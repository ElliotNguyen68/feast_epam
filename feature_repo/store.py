from datetime import datetime
from dateutil.relativedelta import relativedelta

from feast import FeatureStore,repo_config,Entity,FeatureView,FeatureService
from feast.data_source import DataSource
from feast.infra.offline_stores.contrib.spark_offline_store.spark import SparkOfflineStoreConfig
from feast.infra.materialization.contrib.spark.spark_materialization_engine import SparkMaterializationEngineConfig
from feast.infra.online_stores.contrib.postgres import PostgreSQLOnlineStoreConfig

from feature_repo import entities,feature_services,feature_views,get_registry_path

def get_store():
    pgconfig={
        "username":"postgres",
        "password":"testpwd",
        "dbname":"bighead",
        "host":"0.0.0.0",
        "port":5431,
        "schema_name":"public"
    }    
    config_repo = repo_config.RepoConfig(
            provider='local',
            project="bighead",
            registry=repo_config.RegistryConfig(
                path= get_registry_path()
            ),
            offline_store=SparkOfflineStoreConfig(),
            batch_engine_config='spark.engine',
            online_store=PostgreSQLOnlineStoreConfig(
                    host=pgconfig['host'],
                    port=pgconfig.get('port',5432),
                    user=pgconfig['username'],
                    password=pgconfig['password'],
                    database=pgconfig['dbname'],
                    db_schema=pgconfig['schema_name']
                ),
        )
    store=FeatureStore(config=config_repo)
    return store

def apply_store(store:FeatureStore):
    list_entities = [getattr(entities,o) for o in dir(entities) if isinstance(getattr(entities, o),Entity)]
    list_feature_views = [getattr(feature_views,o) for o in dir(feature_views) if isinstance(getattr(feature_views, o),FeatureView)]
    list_feature_services =[getattr(feature_services,o) for o in dir(feature_services) if isinstance(getattr(feature_services, o),FeatureService)]
    list_datasources= [getattr(feature_views,o) for o in dir(feature_views) if isinstance(getattr(feature_views, o),DataSource)]
    
    list_entities_name=list(map(lambda x:x.name,list_entities))
    list_feature_views_name=list(map(lambda x:x.name,list_feature_views))
    list_feature_services_name=list(map(lambda x:x.name,list_feature_services))
    list_datasources_name=list(map(lambda x:x.name,list_datasources))

    previous_entities=store.list_entities()
    previous_feature_views=store.list_feature_views()
    preivous_feature_services=store.list_feature_services()
    preivous_datasources=store.list_data_sources()

    entities_to_delete =[entity for entity in previous_entities if entity.name not in list_entities_name]
    feature_views_delete =[fv for fv in previous_feature_views if fv.name not in list_feature_views_name]
    feature_services_delete =[fs for fs in preivous_feature_services if fs.name not in list_feature_services_name]
    datasources_delete =[ds for ds in preivous_datasources if ds.name not in list_datasources_name]

    store.apply(
        objects=[*list_entities,*list_datasources,*list_feature_services,*list_feature_views],
        objects_to_delete=[
            *entities_to_delete,*datasources_delete,*feature_views_delete,*feature_services_delete
        ],
        partial=False
    )
    
if __name__=='__main__':
    store=get_store()
    apply_store(store=store)
    dt=datetime.now()
    store.materialize(start_date=dt-relativedelta(months=1),end_date=dt)
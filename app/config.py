from cassandra.policies import (
    ConstantSpeculativeExecutionPolicy,
    DowngradingConsistencyRetryPolicy,
    TokenAwarePolicy,
    RoundRobinPolicy
)
from cassandra.cluster import ExecutionProfile, EXEC_PROFILE_DEFAULT
from cassandra.query import dict_factory
from cassandra import ConsistencyLevel


class Config:
    CASSANDRA_KEYSPACE = 'vision'
    CASSANDRA_HOSTS = ['127.0.0.1']
    CASSANDRA_SETUP_KWARGS = dict(
        execution_profiles={
            EXEC_PROFILE_DEFAULT: ExecutionProfile(
                load_balancing_policy=TokenAwarePolicy(RoundRobinPolicy()),
                speculative_execution_policy=ConstantSpeculativeExecutionPolicy(
                    delay=.5,
                    max_attempts=10
                ),
                retry_policy=DowngradingConsistencyRetryPolicy(),
                consistency_level=ConsistencyLevel.LOCAL_QUORUM,
                request_timeout=15,
                row_factory=dict_factory
            )
        },
    )

    PROPAGATE_EXCEPTIONS = False


class DevelopmentConfig(Config):
    CASSANDRA_KEYSPACE = 'test'
    CASSANDRA_HOSTS = ['localhost']


class Production(Config):
    CASSANDRA_RETRY_CONNECT = True


config_by_name = dict(
    development=DevelopmentConfig
)

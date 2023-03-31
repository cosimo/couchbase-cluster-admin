class AddToNotProvisionedNodeException(Exception):
    pass


class BucketCreationException(Exception):
    pass


class ClusterJoinException(Exception):
    pass


class ConnectToControllerOnJoinException(Exception):
    pass


class IllegalArgumentError(ValueError):
    pass


class NodeRenameException(Exception):
    pass


class RebalanceException(Exception):
    pass


class SetAuthenticationException(Exception):
    pass


class SetClusterNameException(Exception):
    pass


class SetMemoryQuotaException(Exception):
    pass


class UserCreationException(Exception):
    pass
import uiautomator2 as u2

d = u2.connect()
timeout = 3


def checkByResourceId(ResourceId):
    """通过resourceid检查"""
    d(resourceId=ResourceId).exists(timeout=timeout)

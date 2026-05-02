from config.settings import settings

ENVIRONMENTS = {
    "dev": {
        "base_url": "https://gtrixdev.serversync.work",
        
    },
    "QA": {
        "base_url": "https://gtrixqa.serversync.work/",
    },
    "demo": {
        "base_url": "https://demo.arkbotech.com.np/",
    },  
    "UAT": {
        "base_url": "https://gtrix.uatserversync.work",
    },
    "prod": {
        "base_url": "https://gtrixprod.serversync.work",
    },
    "local": {
        "base_url": "https://gtrixlocal.serversync.work",
    },
}



def get_base_url() -> str:
    env = settings.ENVIRONMENT.lower()
    if env not in ENVIRONMENTS:
        raise ValueError(f"Unknown environment: {env}")
    return ENVIRONMENTS[env]["base_url"]

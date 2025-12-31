from functools import lru_cache
from os import environ

VERSION = "2026.1.0"
ENV_GIT_HASH_KEY = "GIT_BUILD_HASH"

@lru_cache
def scalelock_version() -> str:
    return VERSION

@lru_cache
def scalelock_build_hash(fallback: str | None = None) -> str:
    build_hash = environ.get(ENV_GIT_HASH_KEY, fallback if fallback else "")
    return fallback if build_hash == "" and fallback else build_hash

@lru_cache
def scalelock_full_version() -> str:
    version = scalelock_version()
    if (build_hash := scalelock_build_hash()) != "":
        return f"{version}+{build_hash}"
    return version
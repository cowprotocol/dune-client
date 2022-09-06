"""
Data Class Representing a Dune Query
"""
import urllib.parse
from dataclasses import dataclass
from typing import Optional

from dune_client.types import QueryParameter


@dataclass
class Query:
    """Basic data structure constituting a Dune Analytics Query."""

    name: str
    query_id: int
    params: Optional[list[QueryParameter]] = None

    def base_url(self) -> str:
        """Returns a link to query results excluding fixed parameters"""
        return f"https://dune.com/queries/{self.query_id}"

    def parameters(self) -> list[QueryParameter]:
        """Non-null version of self.params"""
        return self.params or []

    def url(self) -> str:
        """Returns a parameterized link to the query"""
        # Include variable parameters in the URL so they are set
        params = "&".join([f"{p.key}={p.value}" for p in self.parameters()])
        if params:
            return "?".join(
                [self.base_url(), urllib.parse.quote_plus(params, safe="=&?")]
            )
        return self.base_url()

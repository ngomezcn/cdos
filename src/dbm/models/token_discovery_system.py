from select import select
from sqlalchemy import TIME, Column, UniqueConstraint , create_engine, null
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, VARCHAR, TIMESTAMP, MONEY
from dbm.core.manager import Base

class CryptoTrackingPlatform(Base):
    __tablename__  = 'crypto_tracking_platforms'
    
    ctp_id = Column(VARCHAR, primary_key=True)
    domain = Column(VARCHAR)
    ip = Column(VARCHAR(11))
    root_https = Column(VARCHAR)
           
    def __init__(self, ctp_id, domain, ip, root_https):
        self.ctp_id = ctp_id
        self.domain = domain
        self.ip = ip
        self.root_https = root_https
        
class ScrapedToken(Base):
    __tablename__  = 'scraped_tokens'
    
    pk = None
    uri = Column(VARCHAR, primary_key=True)
    token_id = Column(VARCHAR)
    ctp_id = Column(VARCHAR)
    discovery_timestamp = Column(TIMESTAMP)
    listed_timestamp = Column(TIMESTAMP)
    
    def __init__(self, uri, token_id, ctp_id, discovery_timestamp, listed_timestamp):
        self.uri = uri
        self.token_id = token_id
        self.ctp_id = ctp_id
        self.discovery_timestamp = discovery_timestamp
        self.listed_timestamp = listed_timestamp
        self.pk = uri

class RawDiscoveredToken(Base):      
    __tablename__  = 'raw_discovered_token'
    
    token_id = Column(VARCHAR, primary_key=True)
    url_path = Column(VARCHAR)
    ctp_id = Column(VARCHAR)
    token_name = Column(VARCHAR)
    discovery_timestamp = Column(TIMESTAMP)
    contract = Column(VARCHAR)
    chain_name = Column(VARCHAR)
    price = Column(MONEY)
    listed_timestamp = Column(TIMESTAMP)

    def __init__(self):
        pass
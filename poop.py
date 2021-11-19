import asyncio
import socket
import warnings
from collections import defaultdict
from contextlib import suppress
from typing import Dict, List, Optional

import aiohttp
import discord
from async_rediscache import RedisSession
from discord.ext import commands
from sentry_sdk import push_scope

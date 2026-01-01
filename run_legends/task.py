import time
from webbrowser import get
from utils.client import Client
from utils.utils import (retry, check_res_status, get_utc_now,
                         get_data_lines, sleep, Logger,
                         read_json, Contract, generate_random_hex_string,
                         get_utc_now)
from utils.models import RpcProviders, ChainExplorers, TxStatusResponse
from utils.galxe_utils.captcha import CapmonsterSolver
from utils.galxe_utils.task import GalxeTask
from .config import CONFIG
from .utils import pass_transaction
import random
from utils.galxe_utils.utils import MainGalxeTaskCompleter
from uuid import uuid4


class Task(Logger):
    def __init__(self, session, client: Client, db_manager):
        self.session = session
        self.client = client
        self.db_manager = db_manager
        super().__init__(self.client.address, additional={'pk': self.client.key,
                                                          'proxy': self.session.proxies.get('http')})
        self.explorer = 'https://testnet-explorer.saharalabs.ai/'
        self.captcha_solver = CapmonsterSolver(proxy=self.session.proxies.get('http'),
                                               api_key=CONFIG.SOLVERS.CAPSOLVER_API_KEY,
                                               logger=self.logger)
        self.galxe_task = GalxeTask(session=self.session,
                                    client=self.client,
                                    captcha_solver=self.captcha_solver)

    async def evm_connect(self):
        url = 'https://app-api.quackai.ai/user/evm_connect'

        payload = {'address': self.client.address, 'sign':}

    async def complete_task_1(self):
        url = 'https://app-api.quackai.ai/task/complete_task?taskId=1'

        get

        payload = {'taskId': 1}

    async def complete_task_2(self):
        url = 'https://app-api.quackai.ai/task/complete_task?taskId=2'

        get

        payload = {'taskId': 2}

    async def check_list(self):
        url = f'https://app-api.quackai.ai/task/task_list?address={self.client.address}'

        get

        payload = {'address': self.client.address}

    async def user_info(self):
        url = f'https://app-api.quackai.ai/user/user_info?address={self.client.address}'

    async def conv_list(self):
        url = f'https://app-api.quackai.ai/api/v1/conversations_list?address={self.client.address}'

    async def transaction(self):
        url = f'https://opbnb-mainnet-rpc.bnbchain.org/'

    

    async def self_sender(self):
        pass
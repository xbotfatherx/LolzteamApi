from datetime import datetime
import requests


class NotSetUserid(Exception):
    pass


class LolzteamApi:
    def __init__(self, token: str, userid: int = None, baseUrl="https://api.lzt.market/"):
        self.token = token
        self.userid = userid
        self.baseUrl = baseUrl
        self.session = requests.session()
        self.session.headers = {'Authorization': f'Bearer {self.token}'}

    def get(self, url, params=None):
        if params is None:
            params = {}
        return self.session.get(self.baseUrl + url, params=params).json()

    def post(self, url, data=None):
        if data is None:
            data = {}
        return self.session.post(self.baseUrl + url, data=data).json()

    def put(self, url, data=None):
        if data is None:
            data = {}
        return self.session.put(self.baseUrl + url, data=data).json()

    def delete(self, url, data=None):
        if data is None:
            data = {}
        return self.session.delete(self.baseUrl + url, data=data).json()

    def market_me(self):
        """Displays info about your profile"""

        return self.get(f'me')

    def market_add_proxy(self, proxy_ip: str, proxy_port: int, proxy_user: str = None, proxy_pass: str = None,
                         proxy_row: str = None) -> dict:
        """Add single proxy or proxy list

        To add single proxy use this parameters:
        proxy_ip (required) Proxy ip or host
        proxy_port (required) Proxy port
        proxy_user (optional) Proxy username
        proxy_pass (optional) Proxy password

        To add proxy list use this parameters:
        proxy_row (required) Proxy list in String format ip:port:user:pass. Each proxy must be start with new line,
         (use \r\n separator)
        """
        data = {'proxy_ip': proxy_ip, 'proxy_port': proxy_port}
        if proxy_user:
            data['proxy_user'] = proxy_user
        if proxy_pass:
            data['proxy_pass'] = proxy_pass
        if proxy_row:
            data['proxy_row'] = proxy_row
        return self.post('proxy', data=data)

    def market_delete_proxy(self, proxy_id: int = None, delete_all: bool = False) -> dict:
        """Delete single or all proxies

        Parameters:

        proxy_id (optional) Proxy id
        delete_all (optional) Set boolean if you want to delete all proxy
        """
        if proxy_id:
            data = {'proxy_id': proxy_id}
        elif delete_all:
            data = {'delete_all': True}
        else:
            raise ValueError('Either proxy_id or delete_all must be specified')
        return self.delete('proxy', data=data)

    def market_list_proxy(self):
        return self.get(f'proxy')

    def market_list(self, category: str = None, pmin: int = None, pmax: int = None, title: str = None,
                    parse_sticky_items: str = None, optional: dict = None):
        """Displays a list of latest accounts

        Args:
            category (str, optional): Category on market. Defaults to None.
            pmin (int, optional): Min price for account. Defaults to None.
            pmax (int, optional): Max price for account. Defaults to None.
            title (str, optional): Title for account. Defaults to None.
            parse_sticky_items (str, optional): Condition for parse sticky items. Defaults to None.
            optional (dict, optional): Get from market url params. Defaults to None.
        """
        if category:
            data = {}
            if title: data['title'] = title
            if pmin: data['pmin'] = pmin
            if pmax: data['pmax'] = pmax
            if parse_sticky_items: data['parse_sticky_items'] = parse_sticky_items
            if optional: data = {**data, **optional}
            return self.get(f'{category}', data)
        else:
            return self.get('market')

    def market_orders(self, category: str = None, pmin: int = None, pmax: int = None, title: str = None,
                      showStickyItems: str = None, optional: dict = None):
        """Displays a list of purchased accounts

        Args:
            category (str, optional): Category on market. Defaults to None.
            pmin (int, optional): Min price for account. Defaults to None.
            pmax (int, optional): Max price for account. Defaults to None.
            title (str, optional): Title for account. Defaults to None.
            showStickyItems (str, optional): Condition for parse sticky items. Defaults to None.
            optional (dict, optional): Get from market url params. Defaults to None.

        Raises:
            NotSetUserid: Doesn't set userid in __init__
        """

        if not self.userid:
            raise NotSetUserid
        if category:
            data = {}
            if title: data['title'] = title
            if pmin: data['pmin'] = pmin
            if pmax: data['pmax'] = pmax
            if showStickyItems: data['showStickyItems'] = showStickyItems
            if optional: data = {**data, **optional}
            return self.get(f'user/{self.userid}/orders/{category}', data)
        else:
            return self.get(f'user/{self.userid}/orders')

    def market_fave(self):
        return self.get(f'fave')

    def market_add_star(self, item_id: int):
        return self.post(f'{item_id}/star')

    def market_delete_star(self, item_id: int):
        return self.delete(f'{item_id}/star')

    def market_stick(self, item_id: int):
        return self.post(f'{item_id}/stick')

    def market_unstick(self, item_id: int):
        return self.delete(f'{item_id}/stick')

    def market_change_owner(self, item_id: int, username: str, secret_answer: str):
        return self.post(f'{item_id}/change-owner',
                         data={f'username': username, 'secret_answer': secret_answer})

    def market_set_tag(self, item_id: int, tag_id: int):
        data = {"tag_id": tag_id}
        return self.post(f"{item_id}/tag", data)

    def market_delete_tag(self, item_id: int, tag_id: int):
        data = {"tag_id": tag_id}
        return self.delete(f"{item_id}/tag", data)

    def market_viewed(self):
        return self.get(f'viewed')

    def market_item(self, item):
        return self.get(f'{item}')

    def market_reserve(self, item: int):
        return self.post(f'{item}/reserve',
                         data={'price': self.market_item(item)['item']['price']})

    def market_cancel_reserve(self, item: int):
        return self.post(f'{item}/cancel-reserve')

    def market_check_account(self, item: int):
        return self.post(f'{item}/check-account')

    def market_confirm_buy(self, item: int):
        return self.post(f'{item}/confirm-buy')

    def market_fast_buy(self, item_id: int, price: float, buy_without_validation: int = 0):
        """Check and buy account automatic.
        Args:
            item_id (int): Item id on market
            price (float) (required) Currenct price of account in your currency
            buy_without_validation (int) Put 1 if you want to buy account without account data validation (not safe)
        """
        return self.post(f'{item_id}/fast-buy',
                         data={'price': price, 'buy_without_validation': buy_without_validation})

    def market_transfer(self, receiver: int, receiver_username: str, amount: int, secret_answer: str,
                        currency: str = 'rub', comment: str = None, transfer_hold: str = None,
                        hold_length_value: str = None, hold_length_option: int = None):
        data = {
            'user_id': receiver,
            'username': receiver_username,
            'amount': amount,
            'secret_answer': secret_answer,
            'currency': currency
        }
        if comment: data['comment'] = comment
        if transfer_hold: data['transfer_hold'] = transfer_hold
        if hold_length_value: data['hold_length_value'] = hold_length_value
        if hold_length_option: data['hold_length_option'] = hold_length_option
        return self.post(f'balance/transfer', data)

    def market_payments(self, type_: str = None, pmin: int = None, pmax: int = None, receiver: str = None,
                        sender: str = None, startDate: datetime = None, endDate: datetime = None, wallet: str = None,
                        comment: str = None, is_hold: str = None):
        """Displays list of your payments

        Args:
            type_ (str, optional): Type of operation. Allowed operation types: income cost refilled_balance
            withdrawal_balance paid_item sold_item money_transfer receiving_money internal_purchase claim_hold,
            Defaults to None.
            pmin (int, optional): Minimal price of operation. Defaults to None.
            pmax (int, optional): Maximum price of operation. Defaults to None.
            receiver (str, optional): Username of user, which receive money from you. Defaults to None.
            sender (str, optional): Username of user, which sent money to you. Defaults to None.
            startDate (datetime, optional): Start date of operation (RFC 3339 date format). Defaults to None.
            endDate (datetime, optional): End date of operation (RFC 3339 date format). Defaults to None.
            wallet (str, optional): Wallet, which used for money payots. Defaults to None.
            comment (str, optional): Comment for money transfers. Defaults to None.
            is_hold (str, optional): Display hold operations. Defaults to None.

        Raises:
            NotSetUserid: Doesn't set userid in __init__
        """
        if not self.userid:
            raise NotSetUserid
        data = {}
        if type_: data['type'] = type_
        if pmin: data['pmin'] = pmin
        if pmax: data['pmax'] = pmax
        if receiver: data['receiver'] = receiver
        if sender: data['sender'] = sender
        if startDate: data['startDate'] = startDate
        if endDate: data['endDate'] = endDate
        if wallet: data['wallet'] = wallet
        if comment: data['comment'] = comment
        if is_hold: data['is_hold'] = is_hold
        return self.get(f'user/{self.userid}/payments', data)

    def market_category_params(self, category_name: str):
        """Displays search parameters for a category

        Args:
            category_name (str): Category name
        """
        return self.get(f'{category_name.lower()}/params')

    def market_category_games(self, category_name: str):
        """Displays a list of games in the category

        Args:
            category_name (str): Category name
        """
        return self.get(f'{category_name.lower()}/games')

    def market_add_item(self, title: str, price: int, category_id: int, item_origin: str, extended_guarantee: int,
                        currency: str = 'rub', title_en: str = None, description: str = None, information: str = None,
                        has_email_login_data: bool = None, email_login_data: str = None, email_type: str = None,
                        allow_ask_discount: bool = None, proxy_id: int = None):
        """Adds account on the market.

        Args:
            title (str): title
            price (int): price account in currency
            category_id (int): category id (readme)
            item_origin (str): brute, fishing, stealer, autoreg, personal, resale
            extended_guarantee (int): -1 (12 hours), 0 (24 hours), 1 (3 days)
            currency (str, optional): cny, usd, rub, eur, uah, kzt, byn, gbp. Defaults to 'rub'.
            title_en (str, optional): title english. Defaults to None.
            description (str, optional): public information about account. Defaults to None.
            information (str, optional): private information about account for buyer. Defaults to None.
            has_email_login_data (bool, optional): true or false. Defaults to None.
            email_login_data (str, optional): login:password. Defaults to None.
            email_type (str, optional): native or autoreg. Defaults to None.
            allow_ask_discount (bool, optional): allow ask discount for users. Defaults to None.
            proxy_id (int, optional): proxy id. Defaults to None.
        """
        data = {
            'title': title,
            'price': price,
            'category_id': category_id,
            'currency': currency,
            'item_origin': item_origin,
            'extended_guarantee': extended_guarantee
        }
        if title_en: data['title_en'] = title_en
        if description: data['description'] = description
        if information: data['information'] = information
        if has_email_login_data: data['has_email_login_data'] = has_email_login_data
        if email_login_data: data['email_login_data'] = email_login_data
        if email_type: data['email_type'] = email_type
        if allow_ask_discount: data['allow_ask_discount'] = allow_ask_discount
        if proxy_id: data['proxy_id'] = proxy_id
        return self.post(f'item/add', data=data)

    def market_add_item_check(self, item: int, login: str = None, password: str = None, login_password: str = None,
                              close_item: bool = None):
        """Check account on validity. If account is valid, account will be published on the market.

        Args:
            item (int): Item id on market
            login (str, optional): Account login (or email). Defaults to None.
            password (str, optional): Account password. Defaults to None.
            login_password (str, optional): Account login data format login:password. Defaults to None.
            close_item (bool, optional): If set, the item will be closed item_state = closed. Defaults to None.
        """
        data = {}
        if login: data['login'] = login
        if password: data['password'] = password
        if login_password: data['login_password'] = login_password
        if close_item: data['close_item'] = close_item
        return self.post(f'{item}/goods/check', data)

    def market_get_email(self, item: int, email: str):
        return self.get(f'{item}/email-code', {'email': email})

    def market_refuse_guarantee(self, item: int):
        return self.post(f'{item}/refuse-guarantee')

    def market_change_password(self, item: int):
        return self.post(f'{item}/change-password')

    def market_delete(self, item: int, reason: str):
        return self.delete(f'{item}', {'reason': reason})

    def market_bump(self, item: int):
        return self.post(f'{item}/bump')

    def get_temp_email_password(self, item_id: int):
        """Gets password from temp email of account. After calling of this method, the warranty will be cancelled,
        and you cannot automatically resell account.

        Parameters:
            item_id (int): Item id on market
        """
        return self.get(f'{item_id}/temp-email-password')

    def edit_account_info(self, item_id: int, currency: str = 'rub', key: str = '', value: str = '',
                          key_values=None):
        """Edits any details of account.

        Parameters:

            item_id (int): Item id on market
            key (_optional) Key to edit (key list you can see below). E.g. price.
            value (_optional) Value to edit
            key_values (optional): Dict, example: {'title': 'Account', 'price': 100}
            currency (required) Currency of account price. Required if you are trying to change price field,
            allowed values: cny usd rub eur uah kzt byn gbp
        """
        if key_values is None:
            key_values = {}
        data = {
            'currency': currency
        }
        if key: data['key'] = key
        if value: data['value'] = value
        return self.put(f'{item_id}/edit?' + '&'.join(f'key_values[{k}]={v}' for k, v in key_values.items()),
                        data=data)

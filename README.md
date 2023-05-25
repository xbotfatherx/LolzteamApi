# LOLZTEAM API PYTHON ([сделано на апи](https://github.com/grisha2217/Lolzteam-Public-API/blob/master/docs/market_api.markdown))
По поводу багов/доработок - https://zelenka.guru/nebotfather/
### Init
 * `token` - (__обязательно__) токен api, права *read, post, market*
 * `userid` - userid профиля, необходим для некоторых функций
____
### market_me
Получить информацию маркета о текущем токене
* N/A
____
### market_add_proxy
Добавить прокси
 * `proxy_ip (required)` - айпи
 * `proxy_port (required)` - порт
 * `proxy_user (optional)` - логин
 * `proxy_pass (optional)` - пароль
 
Для добавления списка прокси используйте эти параметры:
        proxy_row (обязательно) Список прокси в строковом формате ip:port:user:pass. Каждый прокси должен начинаться с новой строки,
         (используйте разделитель \r\n)
____
### market_list_proxy
Получить прокси
____
### market_delete_proxy
Удаление одного или всех прокси
 * `proxy_id (optional)` - Айди прокси
 * `delete_all (optional) (bool)` - Используйте `true`, если вы хотите удалить все прокси.
 
Для добавления списка прокси используйте эти параметры:
        `proxy_row (required)` Список прокси в строковом формате ip:port:user:pass. Каждый прокси должен начинаться с новой строки,
         (используйте разделитель \r\n)
___
### market_add_star
Добавить аккаунт в избранное
 * `item_id (required)` - Айди аккаунта на маркете
____
### market_delete_star
Удалить аккаунт из избранного
 * `item_id (required)` - Айди аккаунта на маркете
____
### market_stick
Вывести аккаунт в топ поиска
 * `item_id (required)` - Айди аккаунта на маркете
____
### market_unstick
Вывести аккаунт из топа поиска
 * `item_id (required)` - Айди аккаунта на маркете
____
### market_change_owner
Изменить владельца аккаунта
 * `item_id (required)` - Айди аккаунта на маркете
 * `username (required)` - Имя пользователя нового владельца учетной записи
 * `secret_answer (required)` - Секретная фраза
____
### market_set_tag
Добавить тег аккаунту
 * `item_id (required)` - Айди аккаунта на маркете
 * `tag_id (required)` - id тега
____
### market_delete_tag
Удалить тег аккаунта
 * `item_id (required)` - Айди аккаунта на маркете
 * `tag_id (required)` - id тега
____
### market_list
Получить все последние аккаунты маркеты
 * `category` - категория (словом), если не указано, то возвращает по всем категориям
 * `title` - название товара
 * `pmin` - минимальная цена
 * `pmax` - максмальная цена
 * `parse_sticky_items` - показывать зафиксированные аккаунты
 * `optional` - словарь, с дополнительными параметрами (получаем с маркета)
____
### market_orders
Получить все свои покупки
 * `category` - категория (словом), если не указано, то возвращает по всем категориям
 * `title` - название товара
 * `pmin` - минимальная цена
 * `pmax` - максмальная цена
 * `showStickyItems` - показывать зафиксированные аккаунты
 * `optional` - словарь, с дополнительными параметрами (получаем с маркета)
____
### market_fave
Получить свои избранные товары
* N/A
____
### market_viewed
Получить свои просмотренные товары
* N/A
____
### market_item
Получить свои просмотренные товары
 * `item` - (__обязательно__) id товара
____
### market_fast_buy
Купить аккаунт 
* `item_id (required)` - Айди аккаунта на маркете
* `price (float) (required)` - Текущая цена счета в вашей валюте
* `buy_without_validation (int) (optional)` - 1, если вы хотите купить счет без проверки данных счета (небезопасно)
____
### get_temp_email_password
Получает пароль из временной электронной почты учетной записи. После вызова этого метода гарантия будет аннулирована,
и вы не сможете автоматически перепродать аккаунт.
* `item_id (required)` - Айди аккаунта на маркете
____
### edit_account_info
Редактирует любые детали счета.
* `item_id (int)` - Айди на маркете
* `key (_optional)` - Ключ для редактирования (список ключей вы можете увидеть ниже). Например, цена.
* `value (_optional)` - Значение для редактирования
* `key_values (optional)` - Dict, пример: {'title': 'Account', 'price': 100}
* `currency (required)` - Валюта цены счета. Требуется, если вы пытаетесь изменить поле цены, допустимые значения: cny usd rub eur uah kzt byn gbp
____
### market_reserve
Забронировать товар
 * `item` - (__обязательно__) id товара
____
### market_cancel_reserve
Отменить бронивароние товар
 * `item` - (__обязательно__) id товара
____
### market_check_account
Проверить аккаунт на валидность
 * `item` - (__обязательно__) id товара
____
### market_confirm_buy
Подтвердить покупку (перед этим должно быть бронирование и проверка)
 * `item` - (__обязательно__) id товара
____
### market_transfer
Перевести деньги другому пользователю
 * `receiver` - (__обязательно__) userid получателя
 * `receiver_username` - (__обязательно__) username получателя
 * `amount` - (__обязательно__) сколько переводим
 * `secret_answer` - (__обязательно__) ответ на секретку
 * `currency` - (__обязательно__) валюта, в которой переводим (`cny` `usd` `rub` `eur` `uah` `kzt` `byn` `gbp`)
 * `comment` - комментарий
 * `transfer_hold` - `yes` `no`
 * `hold_length_value` - тип холда (`days` `hours`)
 * `hold_length_option` - значение холда
____
### market_payments
Выводит список транзакций на аккаунте
 * `type_` - `income` `cost` `refilled_balance` `withdrawal_balance` `paid_item` `sold_item` `money_transfer` `receiving_money` `internal_purchase` `claim_hold`
 * `pmin` - минимальная сумма операции
 * `pmax` - максимальная сумма операции
 * `receiver` - ник получателя
 * `sender` - ник отправителя
 * `startDate` - искать с периода (RFC 3339)
 * `endDate` - искать до периода (RFC 3339)
 * `wallet` - кошелек
 * `comment` - комментарий для поиска
 * `is_hold` - `yes` `no` проверка на холд
____
### market_category_params
Получить дополнительные параметры для поиска
 * `categoryName` - (__обязательно__) Название категории
____
### market_category_games
Получить список всех игр в категории
 * `categoryName` - (__обязательно__) Название категории
____
### market_add_item
Добавить товар
 * `type_` - (__обязательно__) `income` `cost` `refilled_balance` `withdrawal_balance` `paid_item` `sold_item` `money_transfer` `receiving_money` `internal_purchase` `claim_hold`
 * `title` - (__обязательно__) название товара
 * `price` - (__обязательно__) цена
 * `category_id` - (__обязательно__) id категории (список категорий внизу)
 * `item_origin` - (__обязательно__) `brute` `fishing` `stealer` `autoreg` `personal` `resale`
 * `extended_guarantee` - (__обязательно__) `-1` 12 часов, `0` 24 часа, `1` 3 дня
 * `currency` - (__обязательно__) валюта (`cny` `usd` `rub` `eur` `uah` `kzt` `byn` `gbp`)
 * `title_en` - название товара на английском
 * `description` - описание публичное
 * `information` - описание для покупателя (появляется после покупки)
 * `has_email_login_data` - `true` `false` есть ли почта
 * `email_login_data` - `login:password` данные от почты (если has_email_login_data=true)
 * `email_type` - `native` родная, `autoreg` авторег
 * `allow_ask_discount` - `true` `false` разрешить просить скидки
 * `proxy_id` - id своих прокси
____
### market_add_item_check
Добавить товар
 * `item` - (__обязательно__) id полученного товара из market_add_item
 * `login` - логин аккаунта
 * `password` - пароль аккаунта
 * `loginpassword` - данные от аккаунта в формате `login:password`
 * `close_item` - закрыть товар
____
### market_get_email
Получить код подтверждения с почты маркета
 * `item` - (__обязательно__) id товара
 * `email` - (__обязательно__) почта аккаунта
____
### market_refuse_guarantee
Отказаться от гарантии
 * `item` - (__обязательно__) id товара
____
### market_change_password
Изменить пароль аккаунта
 * `item` - (__обязательно__) id товара
____
### market_delete
Удалить свой аккаунт с маркета
 * `item` - (__обязательно__) id товара
 * `reason` - (__обязательно__) причина удаления
____
### market_bump
Поднять аккаунт
 * `item` - (__обязательно__) id товара
____
### Список категорий:
 * `1` - Steam
 * `2` - VK
 * `3` - Origin
 * `4` - Warface
 * `5` - Uplay
 * `7` - Social Club
 * `9` - Fortnite
 * `12` - Epic Games
 * `10` - Instagram
 * `11` - BattleNet
 * `14` - World Of Tanks
 * `16` - World Of Tanks Blitz
 * `15` - Supercell
 * `17` - Genshin Impact
 * `18` - Escape From Tarkov
 * `19` - VPN
 * `20` - TikTok
 * `22` - Discord
 * `23` - Cinema
 * `24` - Telegram
 * `25` - YouTube
 * `26`  - Spotify
 * `27` - War Thunder

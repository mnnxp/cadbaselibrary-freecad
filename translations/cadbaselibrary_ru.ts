<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="ru" sourcelanguage="en_US">
<context>
    <name>CADBaseLibrary</name>
    <message>
        <location filename="../CdbsModules/cadbase_library.ui" line="14"/>
        <source>CADBase Library</source>
        <translation>Библиотека CADBase</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library.ui" line="54"/>
        <source>Preview</source>
        <translation>Предпросмотр</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library.ui" line="81"/>
        <source>Options</source>
        <translation>Опции</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library.ui" line="96"/>
        <source>Update list</source>
        <translation>Обновить список</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library.ui" line="142"/>
        <source>Copy link</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library.ui" line="140"/>
        <source>Create component</source>
        <translation>Создание компонента</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library.ui" line="128"/>
        <source>Upload files</source>
        <translation>Выгрузить файлы</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library.ui" line="112"/>
        <source>Settings</source>
        <translation>Настройки</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library.ui" line="144"/>
        <source>Authorization</source>
        <translation>Авторизация</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsEvn.py" line="30"/>
        <source>Location of your existing CADBase library</source>
        <translation>Локальное расположение данных библиотеки CADBase</translation>
    </message>
</context>
<context>
    <name>Component</name>
    <message>
        <location filename="../CdbsModules/cadbase_library_object.ui" line="14"/>
        <source>New component</source>
        <translation>Новый компонент</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_object.ui" line="20"/>
        <source>Create a new component (part) on CADBase platform</source>
        <translation>Создание нового компонента (детали) на платформе CADBase</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_object.ui" line="26"/>
        <source>A new component with the specified name will be created for the authorized user. After successfully creating a new component, the list of favorite components will be updated.</source>
        <translation>Для авторизованного пользователя будет создан новый компонент с указанным именем. После успешного создания нового компонента список избранных компонентов будет обновлен.</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_object.ui" line="38"/>
        <source>Name component</source>
        <translation>Наименование компонента</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_object.ui" line="45"/>
        <source>Enter a name for the new component on CADBase platform</source>
        <translation>Введите имя для нового компонента на платформе CADBase</translation>
    </message>
</context>
<context>
    <name>Config</name>
    <message>
        <location filename="../CdbsModules/cadbase_library_config.ui" line="14"/>
        <source>CADBase Library Configuration</source>
        <translation>Конфигурация библиотеки CADBase</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_config.ui" line="20"/>
        <source>Library path</source>
        <translation>Путь к библиотеке</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_config.ui" line="37"/>
        <source>The addon will use this directory to save downloaded files. Be careful, data in this directory may be overwritten.
Changing the library path will require restarting FreeCAD.</source>
        <translation>Это расширение будет использовать этот каталог для сохранения загруженных файлов. Будьте осторожны, данные в этом каталоге могут быть перезаписаны.
Изменение пути к библиотеке потребует перезапуска FreeCAD.</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_config.ui" line="50"/>
        <source>Enter the path to the local CADBase library.</source>
        <translation>Введите путь к локальной библиотеке CADBase.</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_config.ui" line="69"/>
        <source>...</source>
        <translation>...</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_config.ui" line="83"/>
        <source>Server URL</source>
        <translation>Адрес сервера</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_config.ui" line="91"/>
        <source>Here you can specify the server on which the CADBase platform. Specify the server (URL or IP) if you need to connect to the unofficial CADBase platform server.</source>
        <translation>Здесь указывается адрес сервера, на котором расположена платформа CADBase. Укажите сервер (URL или IP) вручную, если есть необходимость использовать не основной сервер платформы CADBase.</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_config.ui" line="103"/>
        <source>Enter data server URL here</source>
        <translation>Введите адрес сервра тут</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_config.ui" line="113"/>
        <source>Set official</source>
        <translation>Сбросить</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_config.ui" line="127"/>
        <source>Upload settings</source>
        <translation>Настройки выгрузки</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_config.ui" line="135"/>
        <source>By selecting the check boxes below, to change set update process.
If set to `Skip calculate hash`, there will be no comparison between files in local and remote storage. `Forcibly update files` means that files should be uploaded to remote storage without additional checks.</source>
        <translation>Установив значения ниже, можно изменить настройки процесса обновления.
Если установлено значение `Пропускать вычисление хэша`, сравнение файлов в локальном и удаленном хранилищах производиться не будет. `Принудительное обновление файлов` означает, что файлы должны быть загружены в удаленное хранилище без дополнительных проверок.</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_config.ui" line="151"/>
        <source>Skip calculate hash</source>
        <translation>Пропускать вычисление хэша</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_config.ui" line="158"/>
        <source>Forcibly update files</source>
        <translation>Принудительное обновление файлов</translation>
    </message>
</context>
<context>
    <name>Token</name>
    <message>
        <location filename="../CdbsModules/cadbase_library_token.ui" line="14"/>
        <source>Authorization on CADBase</source>
        <translation>Авторизация на CADBase</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_token.ui" line="20"/>
        <source>Authorization</source>
        <translation>Данные для авторизации</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_token.ui" line="26"/>
        <source>CADBase platform access token will be saved locally, after successful authorization.
When the authorization token expires, you will need to request a new authorization token by re-entering your username and password.</source>
        <translation>Токен доступа к платформе CADBase будет сохранен локально после успешной авторизации. 
Когда срок действия токена авторизации истечет, вам нужно будет запросить новый токен авторизации, повторно введя имя пользователя и пароль.</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_token.ui" line="39"/>
        <source>Username</source>
        <translation>Имя пользователя</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_token.ui" line="46"/>
        <source>Enter your username from CADBase</source>
        <translation>Введите имя пользователя от учётной записи CADBase</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_token.ui" line="53"/>
        <source>Password</source>
        <translation>Пароль</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_token.ui" line="63"/>
        <source>Enter your password from CADBase</source>
        <translation>Введите пароль от учётной записи CADBase</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_token.ui" line="72"/>
        <source>Set to create a new user with the specified credentials</source>
        <translation>Устанавливается для создания нового пользователя с указанными учетными данными</translation>
    </message>
</context>
<context>
    <name>UploadFiles</name>
    <message>
        <location filename="../CdbsModules/cadbase_library_upload.ui" line="14"/>
        <source>CADBase Library Upload files</source>
        <translation>Библиотека CADBase Отправка файлов</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_upload.ui" line="20"/>
        <source>Commit message</source>
        <translation>Cообщение о фиксации</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_upload.ui" line="28"/>
        <source>A commit message is a succinct and accurate description of the changes.</source>
        <translation>Сообщение о фиксации или комментарий к изменению - это краткое и ёмкое описание вносимых изменений.</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_upload.ui" line="40"/>
        <source>Enter message here</source>
        <translation>Введите сообщение здесь</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_upload.ui" line="50"/>
        <source>Clear</source>
        <translation>Очистить</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_upload.ui" line="64"/>
        <source>Please waiting data processing...</source>
        <translation>Пожалуйста, подождите, идёт обработка файлов...</translation>
    </message>
    <message>
        <location filename="../CdbsModules/cadbase_library_upload.ui" line="79"/>
        <source>Please note: the changes indicated in the table will be applied only after clicking the OK button.</source>
        <translation>Обратите внимание: изменения, указанные в таблице, будут применены только после нажатия кнопки ОК.</translation>
    </message>
</context>
<context>
    <name>CdbsApi</name>
    <message>
        <location filename="../CdbsModules/CdbsApi.py" line="15"/>
        <source>Successful processing request</source>
        <translation>Успешная обработка запроса</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsApi.py" line="17"/>
        <source>Failed processing request</source>
        <translation>Обработка запроса не удалась</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsApi.py" line="24"/>
        <source>Getting data...</source>
        <translation>Получение данных...</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsApi.py" line="36"/>
        <source>Query include body:</source>
        <translation>Тело запроса:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsApi.py" line="42"/>
        <source>Exception when trying to sending the request:</source>
        <translation>Исключение при попытке отправить запрос:</translation>
    </message>
</context>
<context>
    <name>CdbsAuth</name>
    <message>
        <location filename="../CdbsModules/CdbsAuth.py" line="14"/>
        <source>Successful authorization</source>
        <translation>Успешная авторизация</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsAuth.py" line="16"/>
        <source>Failed authorization</source>
        <translation>Ошибка при авторизации</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsAuth.py" line="23"/>
        <source>Getting a new token, please wait.</source>
        <translation>Получение нового токена, пожалуйста, подождите.</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsAuth.py" line="42"/>
        <source>Exception when trying to login:</source>
        <translation>Исключение при попытке авторизироваться</translation>
    </message>
</context>
<context>
    <name>CdbsStorage</name>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="21"/>
        <source>Preparing for uploading files...</source>
        <translation>Подготовка к загрузке файлов...</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="25"/>
        <source>To upload files, you must select a modification folder or a set of files</source>
        <translation>Для выгрузки файлов необходимо выбрать папку модификации или набора файлов</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="27"/>
        <source>Modification UUID:</source>
        <translation>Идентификатор модификации:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="29"/>
        <source>To upload files, you must select a modification (set of files for FreeCAD will be selected) or a set of files</source>
        <translation>Для выгрузки файлов необходимо выбрать модификацию (будет выбран набор файлов для FreeCAD) или набор файлов</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="38"/>
        <source>Files in the CADBase storage have been updated successfully</source>
        <translation>Файлы в хранилище CADBase успешно обновлены</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="43"/>
        <source>Getting fileset UUID...</source>
        <translation>Получение идентификатора набора файлов</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="48"/>
        <source>Fileset UUID:</source>
        <translation>Идентификатор набора файлов</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="50"/>
        <source>Creating a new set of files for FreeCAD</source>
        <translation>Создание нового набора файлов для FreeCAD</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="55"/>
        <source>Error occurred while getting the UUID of the file set</source>
        <translation>Произошла ошибка при получении UUID набора файлов.</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="63"/>
        <source>Error occurred while confirming the upload of files, the files were not uploaded to correctly</source>
        <translation>Произошла ошибка при подтверждении загрузки файлов, файлы были загружены не правильно</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="67"/>
        <source>No files found for upload</source>
        <translation>Файлы для загрузки не найдены</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="70"/>
        <source>Success upload files to CADBase storage:</source>
        <translation>Файлы успешно загружены в хранилище CADBase:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="80"/>
        <source>Last clicked dir:</source>
        <translation>Последний выбор:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="85"/>
        <source>Local files:</source>
        <translation>Локальные файлы:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="96"/>
        <source>Cloud filenames:</source>
        <translation>Файлы в облаке (удалённом хранилище):</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="100"/>
        <source>The local file has a cloud version:</source>
        <translation>Локальный файл имеет облачную версию</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="104"/>
        <source>Local file does not have a cloud version:</source>
        <translation>Локальный файл не имеет облачную версию</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="116"/>
        <source>Warning: for compare hashes need install `hashlib`. Please try to install it with: `pip install hashlib` or some other way.</source>
        <translation>Внимание: для сравнения хэшей необходимо установить `hashlib`. Пожалуйста, попробуйте установить его с помощью: `pip install hashlib` или каким-либо другим способом.</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="122"/>
        <source>File hash from CADBase not found, this file is skipped:</source>
        <translation>Хэш файла из CADBase не получен, этот файл пропущен:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="126"/>
        <source>Warning: found not file and it skipped</source>
        <translation>Предупреждение: файл не найден и пропущен</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="155"/>
        <source>Uploading files to cloud storage (this can take a long time)</source>
        <translation>Загрузка файлов в облачное хранилище (это может занять много времени)</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="198"/>
        <source>new</source>
        <translation>новый</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="107"/>
        <source>New files to upload:</source>
        <translation>Новые файлы для загрузки:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="211"/>
        <source>deleted</source>
        <translation>удалён</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="203"/>
        <source>Files for deletion:</source>
        <translation>Файлы для удаления:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="115"/>
        <source>Hashlib import error:</source>
        <translation>Ошибка при подключении Hashlib:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="133"/>
        <source>Error calculating hash for local file</source>
        <translation>Ошибка при вычислении хеша для локального файла</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="135"/>
        <source>Hash file</source>
        <translation>Хэш файла</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="135"/>
        <source>local</source>
        <translation>локальный</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="135"/>
        <source>cloud</source>
        <translation>облачное храшилище</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="287"/>
        <source>modified</source>
        <translation>изменён</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="149"/>
        <source>Selected files to upload:</source>
        <translation>Выбранные файлы для загрузки:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="158"/>
        <source>Failed to upload files</source>
        <translation>Не удалось загрузить файлы</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="163"/>
        <source>Confirmation of successful files upload:</source>
        <translation>Подтверждение успешной загрузки файлов:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="172"/>
        <source>Completed upload:</source>
        <translation>Выполнена загрузка:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorage.py" line="182"/>
        <source>Filename:</source>
        <translation>Имя файла:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="91"/>
        <source>time:</source>
        <translation>время:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="97"/>
        <source>sec</source>
        <translation>сек</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="97"/>
        <source>Total time:</source>
        <translation>Общее время:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/UploadTable.py" line="11"/>
        <source>Filename</source>
        <translation>Имя файла</translation>
    </message>
    <message>
        <location filename="../CdbsModules/UploadTable.py" line="12"/>
        <source>Size (local)</source>
        <translation>Размер (локального)</translation>
    </message>
    <message>
        <location filename="../CdbsModules/UploadTable.py" line="13"/>
        <source>Date modified</source>
        <translation>Дата изменения</translation>
    </message>
    <message>
        <location filename="../CdbsModules/UploadTable.py" line="14"/>
        <source>Size (remote)</source>
        <translation>Размер (удалённого)</translation>
    </message>
    <message>
        <location filename="../CdbsModules/UploadTable.py" line="15"/>
        <source>Upload date</source>
        <translation>Дата загрузки</translation>
    </message>
    <message>
        <location filename="../CdbsModules/UploadTable.py" line="16"/>
        <source>Status</source>
        <translation>Состояние</translation>
    </message>
</context>
<context>
    <name>CdbsStorageApi</name>
    <message>
        <location filename="../CdbsModules/CdbsStorageApi.py" line="12"/>
        <source>Preparing for upload file...</source>
        <translation>Подготовка к отправке файла...</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorageApi.py" line="21"/>
        <source>Can not read file...</source>
        <translation>Не могу прочитать файл...</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorageApi.py" line="28"/>
        <source>Upload file...</source>
        <translation>Загрузка файла...</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorageApi.py" line="32"/>
        <source>Exception in upload file:</source>
        <translation>Исключение при загрузке файла:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsStorageApi.py" line="35"/>
        <source>File uploaded. Response bytes:</source>
        <translation>Файл загружен. Содержимое ответа:</translation>
    </message>
</context>
<context>
    <name>DataHandler</name>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="45"/>
        <source>Success</source>
        <translation>Успех</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="48"/>
        <source>Failed, status code:</source>
        <translation>Ошибка, код состояния:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="62"/>
        <source>File already exists and skipped:</source>
        <translation>Файл уже существует и пропущен:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="74"/>
        <source>Exception in download file:</source>
        <translation>Исключение при скачивании файла:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="81"/>
        <source>Error:</source>
        <translation>Ошибка:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="91"/>
        <source>path:</source>
        <translation>путь:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="102"/>
        <source>Data processing, please wait.</source>
        <translation>Обработка данных, пожалуйста, подождите.</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="104"/>
        <source>Not found file with response</source>
        <translation>Не найден файл с ответом</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="111"/>
        <source>Error occurred:</source>
        <translation>Возникла ошибка:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="115"/>
        <source>Exception occurred while parsing the server response:</source>
        <translation>Произошло исключение при анализе ответа сервера:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="121"/>
        <source>No data found to delete</source>
        <translation>Не найдено данных для удаления</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="134"/>
        <source>Exception occurred while trying to save old response:</source>
        <translation>Возникло исключение при попытке сохранить старый ответ:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="139"/>
        <source>removed</source>
        <translation>удалён</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="145"/>
        <source>Please delete this file for correct operation:</source>
        <translation>Пожалуйста, удалите этот файл для корректной работы:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="155"/>
        <source>Exception occurred while trying to write the file:</source>
        <translation>Возникло исключение при попытке записи файла:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="163"/>
        <source>Selected</source>
        <translation>Выбрано</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="166"/>
        <source>Exception when trying to read information from the file:</source>
        <translation>Исключение при попытке прочитать информацию из файла:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="175"/>
        <source>Failed to parse GraphQL before deep parsing:</source>
        <translation>Не удалось получить данные ответа (GraphQL) для дальнейшей обработки:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="180"/>
        <source>Received data is not suitable for processing about</source>
        <translation>Полученны не подходящие для обработки данные о</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="194"/>
        <source>Structure data:</source>
        <translation>Структура данных:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="196"/>
        <source>Not found data for UUID selection:</source>
        <translation>Не найдены данные для выбора UUID:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="199"/>
        <source>Structure vars:</source>
        <translation>Структурные переменные:</translation>
    </message>
    <message>
        <location filename="../CdbsModules/DataHandler.py" line="205"/>
        <source>UUID of structure data:</source>
        <translation>UUID из структуры данных:</translation>
    </message>
</context>
<context>
    <name>cdbs</name>
    <message>
        <location filename="../CdbsModules/CdbsNewUser.py" line="24"/>
        <source>API Point:</source>
        <translation>Адрес сервера (API):</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsNewUser.py" line="25"/>
        <source>New user registration, please wait.</source>
        <translation>Регистрация нового пользователя, пожалуйста, подождите...</translation>
    </message>
    <message>
        <location filename="../CdbsModules/CdbsNewUser.py" line="28"/>
        <source>New user UUID:</source>
        <translation>Идентификатор (UUID) нового пользователя:</translation>
    </message>
</context>
<context>
    <name>CadbaseMacro</name>
    <message>
        <location filename="../CadbaseMacro.py" line="101"/>
        <source>Failed to set path for local library:</source>
        <translation>Не удалось установить путь к локальной библиотеке:</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="106"/>
        <source>Failed with settings base parameters:</source>
        <translation>Не удалось установить основные параметры: </translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="132"/>
        <source>CADBase Library</source>
        <translation>Библиотека CADBase</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="171"/>
        <source>Please update the modification list for this component.</source>
        <translation>Пожалуйста, обновите список модификаций для этого компонента.</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="175"/>
        <source>The link to the selected component has been copied to the clipboard.</source>
        <translation>Ссылка на выбранный компонент вставлена в буфер обмена.</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="177"/>
        <source>Component UUID is not set. Please select a component from the list of favorite components to copy the URL link to the selected component.</source>
        <translation>UUID компонента не установлен. Пожалуйста, выберите компонент из списка избранных компонентов, чтобы скопировать URL-ссылку на выбранный компонент.</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="181"/>
        <source>Unable to find information about a set of files.</source>
        <translation>Невозможно найти информацию о наборе файлов.</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="193"/>
        <source>Token not found</source>
        <translation>Токен не найден</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="215"/>
        <source>Processing the part...</source>
        <translation>Обработка детали...</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="239"/>
        <source>Processing for preview the part...</source>
        <translation>Обработка для предпросмотра детали...</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="260"/>
        <source>CADBase Library Configuration</source>
        <translation>Конфигурация библиотеки CADBase</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="268"/>
        <source>Change information:</source>
        <translation>Информация об изменениях:</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="270"/>
        <source>Change information: no changes were found.</source>
        <translation>Информация об изменениях: изменений не обнаружено.</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="278"/>
        <source>Local location of your existing CADBase library</source>
        <translation>Локальное расположение данных библиотеки CADBase</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="285"/>
        <source>Changes not accepted</source>
        <translation>Изменения отменены</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="294"/>
        <source>Please restart FreeCAD</source>
        <translation>Пожалуйста, перезапустите FreeCAD</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="299"/>
        <source>Configuration updated</source>
        <translation>Конфигурация обновлена</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="305"/>
        <source>Sending a request to create a new user</source>
        <translation>Отправка запроса на создание нового пользователя</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="314"/>
        <source>Library path not found:</source>
        <translation>Путь к библиотеке не найден:</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="322"/>
        <source>Received data about components is not suitable for processing</source>
        <translation>Полученные данные о компонентах не пригодны для обработки.</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="325"/>
        <source>You don&apos;t have favorite components</source>
        <translation>У вас нет избранных компонентов</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="328"/>
        <source>Component UUID:</source>
        <translation>Идентификатор компонента (UUID):</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="332"/>
        <source>Component list update finished</source>
        <translation>Завершенно обновление списка компонентов</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="338"/>
        <source>Not set UUID for select component</source>
        <translation>Не установлен UUID для выбранного компонента</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="343"/>
        <source>It is not possible to create a component without a name</source>
        <translation>Невозможно создать компонент без имени</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="346"/>
        <source>No modifications for the component</source>
        <translation>У компонента нет модификаций</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="350"/>
        <source>Updated the list of modifications to the component</source>
        <translation>Список модификаций компонентa обновлён</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="356"/>
        <source>Not set UUID for select modification</source>
        <translation>Не установлен UUID для выбранной модификации</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="361"/>
        <source>Received data about fileset is not suitable for processing</source>
        <translation>Полученные данные о наборе файлов не подходят для обработки</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="364"/>
        <source>Fileset not found for FreeCAD</source>
        <translation>Набор файлов для FreeCAD не найден</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="369"/>
        <source>Received data about files of fileset is not suitable for processing</source>
        <translation>Получены данные о файлах набора файлов, не пригодны для обработки</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="372"/>
        <source>No files in fileset</source>
        <translation>В наборе файлов нет файлов</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="382"/>
        <source>Download file(s):</source>
        <translation>Скачанных файлов: </translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="383"/>
        <source>Component modification files update completed</source>
        <translation>Файлы модификации компонента обновлены</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="418"/>
        <source>Received data about component is not suitable for processing</source>
        <translation>Полученные данные о компоненте не подходят для обработки</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="505"/>
        <source>Focus shifted to the fileset folder.</source>
        <translation>Фокус переместился на папку с набором файлов.</translation>
    </message>
    <message>
        <location filename="../CadbaseMacro.py" line="513"/>
        <source>The selected file set does not belong to FreeCAD.</source>
        <translation>Выбранный набор файлов не принадлежит FreeCAD.</translation>
    </message>
</context>
<context>
    <name>InitGui</name>
    <message>
        <location filename="../InitGui.py" line="7"/>
        <source>The workbench is designed to use components (parts) from CADBase in the FreeCAD interface. \
Component modifications contain sets of files for various CAD systems. \
This workbench will work with data from the FreeCAD set, without downloading documentation and data from other file sets.</source>
        <translation>Верстак предназначен для использования компонентов (деталей) из CADBase в интерфейсе FreeCAD.
Модификации компонента содержат наборы файлов для различных САПР. \
Этот верстак будет работать данными из набора для FreeCAD, без скачивания документации и данных из других наборов файлов.</translation>
    </message>
    <message>
        <location filename="../InitGui.py" line="8"/>
        <source>CADBase Library</source>
        <translation>Библиотека CADBase</translation>
    </message>
</context>
</TS>

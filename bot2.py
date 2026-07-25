Microsoft Windows [Version 10.0.26200.8894]
(c) Microsoft Corporation. All rights reserved.

C:\Users\User>cd %USERPROFILE%\Documents

C:\Users\User\Documents>mkdir TON-BOT
A subdirectory or file TON-BOT already exists.

C:\Users\User\Documents>cd TON-BOT

C:\Users\User\Documents\TON-BOT>cd TON-BOT python -m pip install python-telegram-bot requests
The system cannot find the path specified.

C:\Users\User\Documents\TON-BOT>python -m pip install python-telegram-bot requests
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: python-telegram-bot in C:\Users\User\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages (22.8)
Requirement already satisfied: requests in C:\Users\User\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages (2.34.2)
Requirement already satisfied: httpx<0.29,>=0.27 in C:\Users\User\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages (from python-telegram-bot) (0.28.1)
Requirement already satisfied: anyio in C:\Users\User\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages (from httpx<0.29,>=0.27->python-telegram-bot) (4.14.2)
Requirement already satisfied: certifi in C:\Users\User\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages (from httpx<0.29,>=0.27->python-telegram-bot) (2026.7.22)
Requirement already satisfied: httpcore==1.* in C:\Users\User\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages (from httpx<0.29,>=0.27->python-telegram-bot) (1.0.9)
Requirement already satisfied: idna in C:\Users\User\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages (from httpx<0.29,>=0.27->python-telegram-bot) (3.18)
Requirement already satisfied: h11>=0.16 in C:\Users\User\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages (from httpcore==1.*->httpx<0.29,>=0.27->python-telegram-bot) (0.16.0)
Requirement already satisfied: charset_normalizer<4,>=2 in C:\Users\User\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages (from requests) (3.4.9)
Requirement already satisfied: urllib3<3,>=1.26 in C:\Users\User\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages (from requests) (2.7.0)

C:\Users\User\Documents\TON-BOT>
C:\Users\User\Documents\TON-BOT>C:\Users\User\Documents\TON-BOT
'C:\Users\User\Documents\TON-BOT' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\User\Documents\TON-BOT>cd
C:\Users\User\Documents\TON-BOT

C:\Users\User\Documents\TON-BOT>notepad bot.py

C:\Users\User\Documents\TON-BOT>dir
 Volume in drive C has no label.
 Volume Serial Number is AF40-C77D

 Directory of C:\Users\User\Documents\TON-BOT

07/25/2026  02:32 PM    <DIR>          .
07/25/2026  02:22 PM    <DIR>          ..
07/25/2026  02:34 PM                21 bot.py
               1 File(s)             21 bytes
               2 Dir(s)  367,246,417,920 bytes free

C:\Users\User\Documents\TON-BOT>python bot.py
Halo TON BOT

C:\Users\User\Documents\TON-BOT>notepad bot.py

C:\Users\User\Documents\TON-BOT>python bot.py
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib\asyncio\runners.py", line 119, in run
    return self._loop.run_until_complete(task)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib\asyncio\base_events.py", line 725, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "C:\Users\User\Documents\TON-BOT\bot.py", line 62, in main
    await asyncio.sleep(60)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib\asyncio\tasks.py", line 720, in sleep
    return await future
           ^^^^^^^^^^^^
asyncio.exceptions.CancelledError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\User\Documents\TON-BOT\bot.py", line 64, in <module>
    asyncio.run(main())
    ~~~~~~~~~~~^^^^^^^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib\asyncio\runners.py", line 196, in run
    return runner.run(main)
           ~~~~~~~~~~^^^^^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib\asyncio\runners.py", line 124, in run
    raise KeyboardInterrupt()
KeyboardInterrupt
^C
C:\Users\User\Documents\TON-BOT>gcd %USERPROFILE%\Documents\TON-BOTpython bot.py
'gcd' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\User\Documents\TON-BOT>notepad bot.py

C:\Users\User\Documents\TON-BOT>python bot.py
'the-open-network'
'the-open-network'

# Internet Speed Test

This a script for a continued speed that generates reports in the **csv format**. The script creates a *csv file* for
each month in the **reports** folder.

## 1 - Running the project

### 1.2 - Requirements

- virtualenv.
- pip.
- virtualenv wrapper.
- python version 3.9 or higher.

### 1.2 - Clone repository

```shell
$ git clone https://github.com/matheusth/InternetSpeedTest.git
```

### 1.3 - Create virtuat enviroment and install requirements.

#### Create virtual enviroment and activate it.

```shell
$ cd InternetSpeedTest
$ virtualenv .venv
$ source .venv/bin/activate
```

#### Install the requirements using **pip**.

```shell
$ pip install -r requirements.txt
```

### 1.4 - run the file *main.py*
```shell
$ python main.py <source-ip-address>
```
# nutters

**nutters** is a simple web application built using [Flask](https://flask.palletsprojects.com/) that displays UPS information polled from systems that run the [Network UPS Tools](https://networkupstools.org/) monitoring daemon. The web application prints out a table listing out each device configured (one per column).

## Set Up

It is recommended that you use virtual environments to install application dependencies and run the application from. After you set up and activate the virtual environment, run the following command to install the required packages.

```bash
venv/bin/python -m pip install -r requirements.txt
```

Replace `venv` with the name of the virtual environment directory in the above command.

## Configuring

### Devices

To define which devices that will be queried by **nutters**, make a copy of the `devices.json.dist` file named `devices.json`. For each device that you want to poll, fill in the following configuration key/value pairs:

| alias | Friendly name of the UPS |
| host | Hostname or IP address of the system running the Network UPS Tools daemon |
| port | The port that the Network UPS Tools daemon is listening on |
| login | Username defined in the Network UPS Tools configuration |
| password | Password for the Network UPS Tools username |
| ups_name | Name of the device defined in the Network UPS Tools configuration |

### Mapping File

In the root of the project directory is a default mapping file, `mappings.json.dist`, that contains a default set of maps between object names presented by Network UPS Tools and descriptive names in the rendered table.

If you would like to modify any of the mappings, make a copy of the default mapping file name and name the file `mappings.json` and the application will load values from that file; otherwise, the application will load values from the default file.

## Hosting

### Configuring Gunicorn

[Gunicorn](https://gunicorn.org/) can take configuration options either as command line arguments or it can load configuration options from a `gunicorn.conf.py` file located in the same directory that Gunicorn is launched from.

A template configuration file is included in the repository called `gunicorn.conf.py.dist`. A copy of that file should be made and named `gunicorn.conf.py` and the configuration options reviewed. The following options may need to be changed depending on the environment in which the application is being deployed:

* `bind`: The template defaults to using a UNIX socket file at
`/tmp/gunicorn-nutters.sock` as the listener. If TCP socket is preferred, change the value to `IP:PORT` (replacing `IP` and `PORT` with the appropriate IP address of the interface and TCP port to listen to)
* `workers`: The number of processes that are created to handle requests.
* `accesslog`: The file that will be used to write access log entries to. Change the value from a string to `None` to disable access logging if that'll be handled by NGINX or a front-end HTTP server.
* `errorlog`: The file that will be used to write error log entries to. Change the value from a string to `None` to disable error logging (not recommended). The directory needs to be created before running the application.

For more information on the above configuration options and other configuration options available, check out the [Gunicorn documentation site](https://docs.gunicorn.org/en/stable/settings.html).

### Setting up a Gunicorn systemd Service

A template `systemd` service file is included in the repository named `gunicorn-nutters.service.dist`. That service file provides the commands and arguments used to start a Gunicorn instance to serve up the application. A copy of that template file can be modified and installed under `/etc/systemd/system`.

For this document, the service file will be installed as `gunicorn-nutters.service` and the service name will be `gunicorn-nutters`. The service file name, thus the service name, can be changed to meet your needs and requirements.

You will need to modify the following items in the new service file:

* `User`: The user which the service will run under
* `Group`: The group which the service will run under
* `WorkingDirectory`: Provide the full path to the application root directory. **Do not** include the `app` directory in the path
* `Environment`: Add the full path to the `venv/bin` directory
* `ExecStart`: Include the full path to the `venv/bin` directory and insert that between `ExecStart=` and `gunicorn`

Save the file and run the following commands to enable and start the new service:

```bash
sudo systemctl enable gunicorn-nutters
sudo systemctl start gunicorn-nutters
```

Verify that the service started by running the following command:

```bash
sudo systemctl status gunicorn-nutters
```

### Serving the Application Through NGINX

Once the service is up and running, NGINX can be configured to proxy requests to Gunicorn. NGINX can also be set up to cache responses and provide additional access controls that may not be feasible with Gunicorn.

Add the following NGINX configuration snippet either to your base `nginx.conf` or to a virtual site configuration file. The configuration settings provides a starting point for serving up the application.

```nginx
upstream gunicorn-nutters {
    server unix:/tmp/gunicorn-nutters.sock fail_timeout=0;
}

server {
    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_pass http://gunicorn-nutters;
    }
}
```

NGINX can also be configured to cache rendered pages to quickly serve up pages that are commonly and frequently requested. NGINX has documentation on configuring and enable proxy caching in their [ngx_http_proxy_module](https://nginx.org/en/docs/http/ngx_http_proxy_module.html) module documentation.

## Code of Conduct

This project follows version 2.1 of the [Contributor Covenant's](https://www.contributor-covenant.org) Code of Conduct.

## License

This application is licensed under the terms of the [MIT License](LICENSE).

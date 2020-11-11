<img src="https://www.ern.com.mx/web/images/logo.png" alt="Oasis LMF logo" width="75"/> <img src="https://oasislmf.org/packages/oasis_theme_package/themes/oasis_theme/assets/src/oasis-lmf-colour.png" alt="Oasis LMF logo" width="250"/>

# ComplexModelMDK

## Run complex model example via MDK
* Install MDK dependent packages, for ubuntu

```
sudo apt-get update && sudo apt-get install libspatialindex-dev unixodbc-dev build-essential libtool zlib1g-dev autoconf
```

* Install OasisLMF (ERN version) and other required packages:

  ```
  pip3 install ./oasislmf/oasislmf-1.9.0-py3-none-manylinux1_x86_64.whl
  pip3 install -r requirements.txt
  ```

* Install the custom item commands and the example custom GulCalc:

  ```
  pip3 install -e .
  ```

* Run the MDK commands, for example:

  ```
  oasislmf model run -C oasislmf.json --verbose
  ```

## Run the complex model example using the API & UI
1) install git, docker and docker-compose

For example on an Ubuntu/Debian based Linux system use:
```
sudo apt update && sudo apt install git docker docker-compose
```

2) Clone this repository
```
git clone https://github.com/HectorERN/PanEuropean
cd PanEuropean
```
3) Run the deployment script
```
sudo ./install.sh
```

4) Access via localhost, using the default `user: admin` `pass: password`
* [OasisUI Interface](http://localhost:8080/app/BFE_RShiny) - *localhost:8080/app/BFE_RShiny* 
* [API Swagger UI](http://localhost:8000/) - *localhost:8000*
* [API Admin Panel](http://localhost:8000/admin) - *localhost:8000/admin*



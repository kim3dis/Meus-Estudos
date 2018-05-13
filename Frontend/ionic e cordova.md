# Configurando o ambiente de desenvolvimento
Instale com os comandos a baixo:

Instale o node.js automatico:
```bash
# node.js v.8:
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs

#node.js v.9:
curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -
sudo apt-get install -y nodejs
```

Instalando node.js no deepin:
```bash
sudo apt-get update
sudo apt-get install build-essential libssl-dev

# algumas distros como deepin não possuem o curl
sudo apt-get install curl

curl -sL https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh -o install_nvm.sh

chmod 755 install_nvm.sh

./install_nvm.sh
nvm ls-remote
nvm install 8.10.0
```


Instale o npm:
```bash
sudo apt install npm
```

Após o Ionic e o Cordova:
```bash
sudo npm install -g ionic
sudo npm install -g cordova

# -g = global; para ter acesso em qualquer parte do sistema;
```

É importante sempre verificar se a instalação teve sucesso, então execute:
```bash
nodejs -v 		# v8.10.0
npm -v 			# 5.6.0
ionic -v 		# 3.20.0
sudo cordova -v # 8.0.0
```


# Primeiro xxc

```bash
ionic --help
```

```bash
ionic start --list
```
>Se não for definido um template, o padrão é tabs.

```bash
# ionic start [nome do projeto] [template]
ionic start HelloWorld tabs
```

Na primeira execução do comando pedirá que você aceite ou não algumas configurações. No meu caso, dei 'y' e segui em frente. Ao final, pedirá para criar-se uma conta no ionic, digite ```ionic signup``` e ele te redirecionará a página de cadastro do ionic.
Após cadastrar-se, faça o login utilizando no terminal ```ionic login```
Utilize novamente o start.
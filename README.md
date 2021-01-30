# combolists-tools
Toolkit for handling email:pass combolists. || Ensemble d'outils pour gérer les combolists email:pass

## USAGE

  **convert.sh <combolist_file>** : This tool will escape all hex characters from <combolist_file>, allowing other tools to run well.

  **validator.py <combolist_file> <result_file>** : This tool will read and extract all combos from <combolist_file> to <result_file>, creating a pure combolist from the given combolist.

  **email.py <combolist_file>** : This tool will read and extract all emails from <combolist_file> to the same file, creating a maillist from the given combolist.

  **cilter.py <maillist>** : This will sort all emails from <maillist> by domain and put them in the _Domains/_ folder. 
  
  For example, _"Domains/gmail.com"_ will contain emails like xxx@gmail.com, and _"Domains/comcast.net"_ will contain emails like xxx@comcast.net.
  
  **country.py** : This will sort all maillists in the _Domains_ folder by country.  
 
  Let's assume that the content of the _Domains_ folder contains the files _yahoo.co.uk, gmail.com, comcast.net, otakufr.com_.
  After running country.py, _"Domains"_ will contain folders like _Domains/com, Domains/uk and Domains/net_.
  ##### Mostly all apps here should be running on Python3 on Linux for better speed ^_^


## UTILISATION

  ** convert.sh <combolist_file> **: Cet outil échappera tous les caractères hexadécimaux de <combolist_file>, permettant aux autres outils de bien fonctionner.

  ** validator.py <combolist_file> <result_file> **: Cet outil lira et extraira tous les combos de <combolist_file> à <result_file>, créant un combolist pur à partir du combolist donné.

  ** email.py <combolist_file> **: Cet outil lira et extraira tous les e-mails de <combolist_file> vers le même fichier, créant une liste de maillages à partir de la liste combinée donnée.

  ** cilter.py <maillist> **: Cela triera tous les e-mails de <maillist> par domaine et les placera dans le dossier _Domains / _.
  
  Par exemple, _ "Domains / gmail.com" _ contiendra des e-mails comme xxx@gmail.com, et _ "Domains / comcast.net" _ contiendra des e-mails comme xxx@comcast.net.
  
  ** country.py **: Cela triera tous les maillists du dossier _Domains_ par pays.
 
  Supposons que le contenu du dossier _Domains_ contient les fichiers _yahoo.co.uk, gmail.com, comcast.net, otakufr.com_.
  Après avoir exécuté country.py, _ "Domains" _ contiendra des dossiers tels que _Domains / com, Domains / uk et Domains / net_.
  ##### La plupart des applications ici devraient fonctionner sur Python3 sous Linux pour une meilleure vitesse ^ _ ^

##LICENCE
  These tools are free to use, so you all can use it as you wish but don't sell them.
  ###### by m1ckT3sl4 ^_^ 

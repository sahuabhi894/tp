from git import Repo

#Repo.clone_from(git_url, repo_dir)

def cpmt():
    import os
    os.chdir('/content')
    CODE_DIR = 'SAM'
    Repo.clone_from("https://github.com/yuval-alaluf/SAM.git","$CODE_DIR")
    #!git clone https://github.com/yuval-alaluf/SAM.git $CODE_DIR
    Repo.clone_from("https://github.com/yuval-alaluf/SAM.git","$CODE_DIR")
    import wget
    url = 'https://github.com/ninja-build/ninja/releases/download/v1.8.2/ninja-linux.zip'
    filename = wget.download(url)
    #!wget https://github.com/ninja-build/ninja/releases/download/v1.8.2/ninja-linux.zip
    sudo apt-get install unzip
    unzip file.zip -d /usr/local/bin/
    #!sudo unzip ninja-linux.zip -d /usr/local/bin/
    #!sudo update-alternatives --install /usr/bin/ninja ninja /usr/local/bin/ninja 1 --force 

Steps to access bitbucket-ADaPT repository.
1. Browse the url : https://innersource.accenture.com
2. Search for repo "ADaPT" on the search bar.
3. Log in to your local computer as an administrator.
    ssh-keygen -t rsa -C "your_email@example.com" 
4.Just press <Enter> to accept the default location and file name. If the .ssh directory doesn't exist, the system creates one for you.
5.Enter, and re-enter, a passphrase when prompted(Optional step).
6.Now search for your ssh keys under C:/Users/yourname/.ssh.
7.There would be 2 files id_rsa(private one) and id_rsa.pub(public one).
8.Go to "ADaPT" repository, left panel Click on settings , then go to "Access Keys".
9.Click on the button "Add key".
10.Text box will appear , select the radio button "Read/write". And paste your public key on the textbox save it.
11.Then go to cmd or gitbash, need to execute the below commands before you can push the code.
  a)git config --global user.name "Mohapatra, Smita"
    git config --global user.email "email@abc.com"
  b)Clone the repo
    git clone ssh://git@innersource.accenture.com/~smita.mohapatra/adapt.git
  c)My code is ready to be pushed
	If you already have code ready to be pushed to this repository then run this in your terminal.

    cd /path/clonedrepo/
    git add --all
    git commit -m "Initial Commit"
    git remote add origin ssh://git@innersource.accenture.com/~smita.mohapatra/adapt.git
    git push -u origin HEAD:master



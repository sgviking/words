# Words API

## Install / Configure Words API  

The Words API server can be configured by running the words.yml playbook with
the following command.  

```
ansible-playbook -i production -u ubuntu --ask-vault-pass words.yml  
```

The vault password is the same password as the API user.  

## Testing Words API  

The words_tiny.json, words_small.json and words_large.json can be used to test  
the Words API with the curl command (replace pasword with bob's actual
password).  

```
curl -d@words_small.json -k -u "bob:password" https://159.203.202.59/  
```

The current implementation of the Words API on the production server with  
500M of RAM will handle ~12M of input.  Notes for addressing this can be  
found in src/lib/utils.py  

The structure of the json submitted to the API looks like this.  

```
{  
    "text": "Words go here, here and here.  Don't put them here"  
}  
```

## Remove derpsie service  

To remove the derpsie service that is listening on port 443 (causing NGINX to  
fail), run the remove_derpsie.yml playbook with the following command.  

```
ansible-playbook -i production -u ubuntu --ask-vault-pass remove_derpie.yml  
```


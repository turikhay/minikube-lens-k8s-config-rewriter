# Minikube-inside-WSL config rewrite

A (very) hacky workaround to allow [Lens](https://k8slens.dev/) to connect to Minikube inside WSL.

See [lens#5714](https://github.com/lensapp/lens/issues/5714)

## Prerequesties

1. Clone this project inside WSL
2. `sudo apt install python3 python3-pip python3-venv`
3. Activate venv with `source venv/bin/activate`
4. Install dependencies `pip install -r requirements.txt`

## Usage

1. Install [Minikube](https://minikube.sigs.k8s.io/docs/start/) inside WSL and [Lens](https://k8slens.dev/) inside Windows host
2. Create `.env` from `.env.sample`
3. Start minikube with `minikube-start.sh`

<details>
  <summary>💡 Add this script to your $PATH</summary>

```shell
$ ln -s minikube-start.sh ~/bin/minikube-start
```
  
</details>
<br/>

4. Lens should pick up Minikube cluster

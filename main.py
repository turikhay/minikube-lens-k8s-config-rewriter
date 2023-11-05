import os
from dotenv import load_dotenv
from subprocess import run
from pathlib import Path
from io import StringIO
from yaml import load, dump, Loader, Dumper

def rewrite_kube_config(src: str, dest_file: str):
    assert isinstance(src, str)
    assert isinstance(dest_file, str)
    config = load(StringIO(src), Loader)
    assert config["kind"] == "Config"
    for cluster_info in config["clusters"]:
        if cluster_info["name"] != "minikube":
            continue
        cluster = cluster_info["cluster"]
        cluster["certificate-authority"] = rewrite_path(cluster["certificate-authority"])
        break
    for user_info in config["users"]:
        if user_info["name"] != "minikube":
            continue
        user = user_info["user"]
        user["client-certificate"] = rewrite_path(user["client-certificate"])
        user["client-key"] = rewrite_path(user["client-key"])
        break
    with open(dest_file, "w") as f:
        dump(config, f, Dumper)

def rewrite_path(p: str, to_windows=True) -> str:
    assert isinstance(p, str)
    return run_shell(["wslpath", "-w" if to_windows else "-u", p])

def run_shell(cmd: str | list[str]) -> str:
    result = run(
        cmd,
        shell=isinstance(cmd, str),
        capture_output=True,
        text=True, check=True, timeout=5
    )
    output = result.stdout.strip()
    return output

if __name__ == "__main__":
    load_dotenv()
    dest_file = os.environ.get("DEST_KUBE_CONFIG")
    print(f"Rewriting config to {dest_file}")
    rewrite_kube_config(
        run_shell("kubectl config view"),
        rewrite_path(dest_file, to_windows=False)
    )
    print("OK")

from uvicorn import run as uvirun

from server.config import check_settings

if __name__ == "__main__":
    exit_code = 0
    exit_code += check_settings()
    if exit_code == 0:
        uvirun("server.main:app", host="0.0.0.0", port=80, proxy_headers=True,
               use_colors=True, workers=2, forwarded_allow_ips="*")
    exit(exit_code)
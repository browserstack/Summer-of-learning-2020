pytest -n 5  parallel/remote_site_tests.py --driver Chrome --os-version 10 &  PIDCHROME10=$!
pytest -n 5  parallel/remote_site_tests.py --driver Chrome --os-version 8.1 &  PIDCHROME8_1=$!
pytest -n 5  parallel/remote_site_tests.py --driver Chrome --os-version 8.1 &  PIDCHROME8=$!
pytest -n 5  parallel/remote_site_tests.py --driver Firefox --os-version 10 &  PIDFIREFOX10=$!
pytest -n 5  parallel/remote_site_tests.py --driver Firefox --os-version 8.1 &  PIDFIREFOX8_1=$!
pytest -n 5  parallel/remote_site_tests.py --driver Firefox --os-version 8 &  PIDFIREFOX8=$!
pytest -n 5  parallel/remote_site_tests.py --driver Edge --os-version 10 &  PIDEDGE10=$!
pytest -n 5  parallel/remote_site_tests.py --driver Edge --os-version 8.1 &  PIDEDGE8_1=$!
pytest -n 5  parallel/remote_site_tests.py --driver Edge --os-version 8 &  PIDEDGE8=$!
pytest -n 5  parallel/remote_site_tests.py --driver IE  --os-version 10 &  PIDIE10=$!
pytest -n 5  parallel/remote_site_tests.py --driver IE  --os-version 8.1 &  PIDIE81=$!
pytest -n 5  parallel/remote_site_tests.py --driver IE  --os-version 8 &  PIDIE8=$!
pytest -n 5  parallel/remote_site_tests.py --driver IE  --os-version 7 &  PIDIE7=$!
pytest -n 5  parallel/remote_site_tests.py --driver Safari --os "OS X" --os-version Catalina &  PIDSAFARICAT=$!
pytest -n 5  parallel/remote_site_tests.py --driver Safari --os "OS X" --os-version Mojave &  PIDSAFARIMOJ=$!
pytest -n 5  parallel/remote_site_tests.py --driver Safari --os "OS X" --os-version "High Sierra" &  PIDSAFARIHS=$!
pytest -n 5  parallel/remote_site_tests.py --driver Safari --os "OS X" --os-version Sierra &  PIDSAFARISIE=$!
pytest -n 5  parallel/remote_site_tests.py --driver Safari --os "OS X" --os-version "El Capitan" &  PIDSAFARIELC=$!
pytest -n 5  parallel/remote_site_tests.py --driver 'Galaxy S20' &  PIDGALAXY=$!
pytest -n 5  parallel/remote_site_tests.py --driver ios &  PIDSAFARI=$!

wait
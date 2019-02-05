VERSION=`grep "__version__" lutris/__init__.py | cut -d" " -f 3 | sed 's|"\(.*\)"|\1|'`

cover:
	rm tests/fixtures/pga.db -f
	rm tests/coverage/ -rf
	nosetests --with-coverage --cover-package=lutris --cover-html --cover-html-dir=tests/coverage

test:
	rm tests/fixtures/pga.db -f
	nosetests
	flake8 lutris

deb-source: clean
	gbp buildpackage -S --git-debian-branch=${GITBRANCH}
	mkdir -p build
	mv ../lutris_0* build

deb: clean
	gbp buildpackage --git-debian-branch=${GITBRANCH}
	mkdir -p build
	mv ../lutris_0* build

changelog-add:
	EDITOR=vim dch -i

changelog-edit:
	EDITOR=vim dch -e

clean:
	rm -rf build
	debclean

build-all: deb

upload:
	scp build/lutris_${VERSION}.tar.xz lutris.net:/srv/releases/

pgp-renew:
	osc signkey --extend home:strycore
	osc rebuildpac home:strycore --all

generate-pot:
	pygettext -o po/lutris.pot lutris

generate-mo:
	mkdir -p share/locale/cs/LC_MESSAGES
	pocompile -i po/cs.po -o share/locale/cs/LC_MESSAGES/lutris.mo
	mkdir -p share/locale/de/LC_MESSAGES
	pocompile -i po/de.po -o share/locale/de/LC_MESSAGES/lutris.mo
	mkdir -p share/locale/es/LC_MESSAGES
	pocompile -i po/es.po -o share/locale/es/LC_MESSAGES/lutris.mo
	mkdir -p share/locale/fr/LC_MESSAGES
	pocompile -i po/fr.po -o share/locale/fr/LC_MESSAGES/lutris.mo
	mkdir -p share/locale/gl/LC_MESSAGES
	pocompile -i po/gl.po -o share/locale/gl/LC_MESSAGES/lutris.mo
	mkdir -p share/locale/id/LC_MESSAGES
	pocompile -i po/id.po -o share/locale/id/LC_MESSAGES/lutris.mo
	mkdir -p share/locale/ko/LC_MESSAGES
	pocompile -i po/ko.po -o share/locale/ko/LC_MESSAGES/lutris.mo
	mkdir -p share/locale/nl_NL/LC_MESSAGES
	pocompile -i po/nl_NL.po -o share/locale/nl_NL/LC_MESSAGES/lutris.mo
	mkdir -p share/locale/pl/LC_MESSAGES
	pocompile -i po/pl.po -o share/locale/pl/LC_MESSAGES/lutris.mo
	mkdir -p share/locale/pt-br/LC_MESSAGES
	pocompile -i po/pt-br.po -o share/locale/pt-br/LC_MESSAGES/lutris.mo
	mkdir -p share/locale/ru/LC_MESSAGES
	pocompile -i po/ru.po -o share/locale/ru/LC_MESSAGES/lutris.mo
	mkdir -p share/locale/sv/LC_MESSAGES
	pocompile -i po/sv.po -o share/locale/sv/LC_MESSAGES/lutris.mo
	mkdir -p share/locale/tr/LC_MESSAGES
	pocompile -i po/tr.po -o share/locale/tr/LC_MESSAGES/lutris.mo

winetricks:
	wget https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks -O share/lutris/bin/winetricks

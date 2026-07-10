%global tl_name algxpar
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.99.2a
Release:	%{tl_revision}.1
Summary:	Support multiple lines of pseudocode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/algxpar
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/algxpar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/algxpar.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(algorithmicx)
Requires:	texlive(amsfonts)
Requires:	texlive(etoolbox)
Requires:	texlive(pgf)
Requires:	texlive(pgfopts)
Requires:	texlive(ragged2e)
Requires:	texlive(varwidth)
Requires:	texlive(xcolor)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package extends the package algorithmicx to support long text which
spans over multiple lines.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/algxpar
%dir %{_datadir}/texmf-dist/tex/latex/algxpar
%doc %{_datadir}/texmf-dist/doc/latex/algxpar/DEPENDS.txt
%doc %{_datadir}/texmf-dist/doc/latex/algxpar/README.md
%doc %{_datadir}/texmf-dist/doc/latex/algxpar/algxpar-doc.pdf
%doc %{_datadir}/texmf-dist/doc/latex/algxpar/algxpar-doc.tex
%doc %{_datadir}/texmf-dist/doc/latex/algxpar/license
%{_datadir}/texmf-dist/tex/latex/algxpar/algxpar-brazilian.kw.tex
%{_datadir}/texmf-dist/tex/latex/algxpar/algxpar-english.kw.tex
%{_datadir}/texmf-dist/tex/latex/algxpar/algxpar.sty

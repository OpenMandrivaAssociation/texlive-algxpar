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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
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


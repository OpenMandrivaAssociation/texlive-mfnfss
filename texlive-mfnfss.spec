Name:		texlive-mfnfss
Version:	46036
Release:	2
Summary:	Packages to typeset oldgerman and pandora fonts in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mfnfss
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mfnfss.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mfnfss.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mfnfss.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle contains two packages: - oldgerm, a package to
typeset with old german fonts designed by Yannis Haralambous. -
pandora, a package to typeset with Pandora fonts designed by
Neena Billawala. Note that support for the Pandora fonts is
also available via the pandora-latex package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mfnfss
%doc %{_texmfdistdir}/doc/latex/mfnfss
#- source
%doc %{_texmfdistdir}/source/latex/mfnfss

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

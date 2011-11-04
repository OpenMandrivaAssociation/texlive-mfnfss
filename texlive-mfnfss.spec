# revision 19410
# category Package
# catalog-ctan /macros/latex/contrib/mfnfss
# catalog-date 2010-07-12 11:01:48 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-mfnfss
Version:	20100712
Release:	1
Summary:	Packages to typeset oldgerman and pandora fonts in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mfnfss
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mfnfss.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mfnfss.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mfnfss.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This bundle contains two packages: - oldgerm, a package to
typeset with old german fonts designed by Yannis Haralambous. -
pandora, a package to typeset with Pandora fonts designed by
Neena Billawala. Note that support for the Pandora fonts is
also available via the pandora-latex package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mfnfss/oldgerm.sty
%{_texmfdistdir}/tex/latex/mfnfss/ot1panr.fd
%{_texmfdistdir}/tex/latex/mfnfss/ot1pss.fd
%{_texmfdistdir}/tex/latex/mfnfss/pandora.sty
%{_texmfdistdir}/tex/latex/mfnfss/uyfrak.fd
%{_texmfdistdir}/tex/latex/mfnfss/uygoth.fd
%{_texmfdistdir}/tex/latex/mfnfss/uyinit.fd
%{_texmfdistdir}/tex/latex/mfnfss/uyswab.fd
%doc %{_texmfdistdir}/doc/latex/mfnfss/changes.txt
%doc %{_texmfdistdir}/doc/latex/mfnfss/manifest.txt
%doc %{_texmfdistdir}/doc/latex/mfnfss/oldgerm.pdf
%doc %{_texmfdistdir}/doc/latex/mfnfss/readme.txt
#- source
%doc %{_texmfdistdir}/source/latex/mfnfss/oldgerm.dtx
%doc %{_texmfdistdir}/source/latex/mfnfss/oldgerm.ins
%doc %{_texmfdistdir}/source/latex/mfnfss/pandora.dtx
%doc %{_texmfdistdir}/source/latex/mfnfss/pandora.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

%global tl_name mfnfss
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Packages to typeset oldgerman and pandora fonts in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mfnfss
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mfnfss.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mfnfss.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mfnfss.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle contains two packages: - oldgerm, a package to typeset with
old german fonts designed by Yannis Haralambous. - pandora, a package to
typeset with Pandora fonts designed by Neena Billawala. Note that
support for the Pandora fonts is also available via the pandora-latex
package.


Name:		texlive-xduthesis
Version:	63116
Release:	1
Summary:	XeLaTeX template for writing Xidian University Thesis
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xduthesis
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xduthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xduthesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xduthesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a XeLaTeX template for writing theses to apply academic
degrees in Xidian University. The template is designed
according to the official requirements on typesetting theses.
The template currently supports all levels of degrees from
bachelor to doctor, including both academic master and
professional master. But it is not guaranteed that you will
pass the typesetting check and obtain your degree by using this
template.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/xduthesis
%{_texmfdistdir}/tex/latex/xduthesis
%doc %{_texmfdistdir}/doc/latex/xduthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

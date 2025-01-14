Name:		texlive-randtext
Version:	15878
Release:	2
Summary:	Randomise the order of characters in strings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/randtext/randtext.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/randtext.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/randtext.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a single macro \randomize{TEXT} that
typesets the characters of TEXT in random order, such that the
resulting output appears correct, but most automated attempts
to read the file will misunderstand it. This function allows
one to include an email address in a TeX document and publish
it online without fear of email address harvesters or spammers
easily picking up the address.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/randtext
%doc %{_texmfdistdir}/doc/latex/randtext

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/randtext/randtext.sty
# catalog-date 2007-02-26 00:17:56 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-randtext
Version:	20070226
Release:	1
Summary:	Randomise the order of characters in strings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/randtext/randtext.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/randtext.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/randtext.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The package provides a single macro \randomize{TEXT} that
typesets the characters of TEXT in random order, such that the
resulting output appears correct, but most automated attempts
to read the file will misunderstand it. This function allows
one to include an email address in a TeX document and publish
it online without fear of email address harvesters or spammers
easily picking up the address.

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
%{_texmfdistdir}/tex/latex/randtext/randtext.sty
%doc %{_texmfdistdir}/doc/latex/randtext/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

Summary:	WepLab, analyzing WEP encryption security on wireless networks
Summary(pl):	WepLab - analizator szyfrowania WEP w sieciach bezprzewodowych
Name:		weplab
Version:	0.1.5
Release:	1
License:	GPL v2
Group:		Networking
Source0:	http://dl.sourceforge.net/weplab/%{name}-%{version}.tar.gz
# Source0-md5:	713870965447b0b8b7341409968846fb
URL:		http://weplab.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel >= 2:0.8.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WepLab is a tool designed to teach how WEP works, what different
vulnerabilities it has, and how they can be used in practice to break
a WEP protected wireless network.

%description -l pl
WepLab to narzêdzie do nauki jak dzia³a WEP, jakie ma s³abo¶ci i
jak mog± byæ one wykorzystane do z³amania sieci bezprzewodowej
zabezpieczonej przez WEP.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=%{_prefix} \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

Summary:	WepLab, analyzing WEP encryption security on wireless networks
Summary(pl):	WepLab, analizator szyfrowania WEP w sieciach bezprzewodowych
Name:		weplab
Version:	0.1.4
Release:	1
License:	GPL v2
Group:		Networking
Source0:	http://dl.sourceforge.net/weplab/%{name}-%{version}.tar.gz
# Source0-md5:	72531c9eec8dc716c87326fc2aa9a0f5
URL:		http://weplab.sourceforge.net/
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WepLab is a tool designed to teach how WEP works, what different
vulnerabilities it has, and how they can be used in practice to break
a WEP protected wireless network.

%description -l pl
WepLab to narzêdzie do uczenia siê jak dzia³a WEP, jakie ma s³abo¶ci i
jak mog± byæ one wyko¿ystane by z³amaæ WEP'a w sieciach
bezprzewodowych.

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

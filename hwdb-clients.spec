Summary:	Hardware database clients
Name:		hwdb-clients
Version:	0.18
Release:	%mkrel 4
License:	GPL
Group:		System/Base
URL:		http://qa.mandriva.com/
Source0:	%{name}-%{version}.tar.bz2
Requires:	drakxtools >= 10-32mdk, dmidecode sane-backends, perl-libwww-perl
Provides:	testzilla-clients
Obsoletes:	testzilla-clients
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Clients to dialog with a hardware database.

%prep
%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/hwdb

# MAKE THE MODIFICATIONS IN THE CVS. NO DIRECT EDITION OR PATCH ALLOWED.



Summary:	Hardware database clients
Name:		hwdb-clients
Version:	0.18
Release:	10
License:	GPLv2
Group:		System/Base
Url:		http://qa.mandriva.com/
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch
Requires:	drakxtools
Requires:	dmidecode
Requires:	sane-backends
Requires:	perl-libwww-perl

%description
Clients to dialog with a hardware database.

%prep
%setup -q

%build

%install
%makeinstall_std

%files
%doc ChangeLog
%{_sbindir}/*
%{_datadir}/hwdb


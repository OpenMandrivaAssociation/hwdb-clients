Summary:	Hardware database clients
Name:		hwdb-clients
Version:	0.18
Release:	%mkrel 7
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




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.18-7mdv2011.0
+ Revision: 665487
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.18-6mdv2011.0
+ Revision: 605886
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.18-5mdv2010.1
+ Revision: 522870
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.18-4mdv2010.0
+ Revision: 425193
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.18-3mdv2009.0
+ Revision: 221390
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.18-2mdv2008.1
+ Revision: 126890
- kill re-definition of %%buildroot on Pixel's request


* Mon Feb 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.18-2mdv2007.0
+ Revision: 119959
- Import hwdb-clients

* Wed Sep 14 2005 Frederic Lepied <flepied@mandriva.com> 0.18-1mdk
- report the IEEE1284 string in the record of printers
- don't translate to avoid having some strange printer names in the database

* Thu Jul 28 2005 Frederic Lepied <flepied@mandriva.com> 0.17-1mdk
- mandriva
- mkrel

* Thu Mar 31 2005 Frederic Lepied <flepied@mandrakesoft.com> 0.16.1-1mdk
- report unknown printers on output
- fix storage raid detection

* Fri Oct 01 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.16-1mdk
- added mouse, tablet and keyboard support (only USB)

* Wed Sep 15 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.15.2-1mdk
- better handling of unknown and scanner classes

* Tue Sep 07 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.15.1-1mdk
- use hwdb.mandrakesoft.com as the server name
- fixed some perl_checker warnings
- don't install hwdb_test twice
- corrected modem support to not forget serial ones ;-) (bug #11177)
- added memory controller (bug #11172)

* Sat Sep 04 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.15-1mdk
- added modem
- addem UPS
- added unknown
- added SATA RAID controller
- added hwdb_test script to be able to debug

* Wed Aug 25 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.14-1mdk
- add back usb printer upload (bug #8642)

* Sat Aug 21 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.13.1-1mdk
- allow to put the password in the HWDB_PASSWD environment variable

* Sat Aug 07 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.13-1mdk
- added cpu support
- added controller support

* Wed Aug 04 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.12-1mdk
- added usb storage and adsl device support
- temporarily remove broken usb printer support (bug #8642)
- hwdb_add_system takes an extra parameter to be able to identify the
uploaded system by a name

* Thu May 13 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.11-1mdk
- adapt hwdb-client for new harddrake data structure (bug #8136)

* Tue Feb 24 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.10-1mdk
- use http_proxy environment variable (bug #8042)
- testzilla => hwdb

* Thu Feb 12 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.9-1mdk
- added WEBCAM support


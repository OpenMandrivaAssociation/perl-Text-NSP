%define upstream_name	 Text-NSP
%define upstream_version 1.27
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	The Ngram Statistics Package 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/Text-NSP-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The module NSP.pm is a stub that doesn't have any real functionality. The real
work is done by five programs:
- count.pl
- statistic.pl
- rank.pl
- combig.pl
- kocos.pl
These are not modules, and are run from the command line. All have extensive
command line help and documentation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES README doc/*
%{perl_vendorlib}/Text
%{_mandir}/*/*
%{_bindir}/*

%changelog
* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.230.0-1mdv2011.0
+ Revision: 654381
- update to new version 1.23

* Wed Nov 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.210.0-1mdv2011.0
+ Revision: 598378
- update to new version 1.21

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.170.0-1mdv2011.0
+ Revision: 552673
- update to 1.17

* Fri Apr 09 2010 Jérôme Quelin <jquelin@mandriva.org> 1.150.0-1mdv2010.1
+ Revision: 533393
- update to 1.15

* Sun Mar 07 2010 Jérôme Quelin <jquelin@mandriva.org> 1.130.0-1mdv2010.1
+ Revision: 515369
- update to 1.13

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.110.0-1mdv2010.1
+ Revision: 461358
- update to 1.11

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.90.0-1mdv2010.0
+ Revision: 405713
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.09-2mdv2009.0
+ Revision: 268795
- rebuild early 2009.0 package (before pixel changes)

* Thu Apr 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-1mdv2009.0
+ Revision: 195102
- fix documentation files location

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-2mdv2008.1
+ Revision: 133669
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Sep 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdv2007.0
- New version 1.03

* Mon Jun 26 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2007.0
- New version 1.01

* Fri Jun 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.99-1mdv2007.0
- new version
- drop patch, useless anymore

* Tue Jun 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.95-1mdv2007.0
- New version 0.95
- rediff installation patch

* Mon Apr 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.91-1mdk
- New release 0.91
- rediff installation patch

* Wed Nov 16 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.73-2mdk
- install main module man page too 
- install pod documentation

* Wed Nov 16 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.73-1mdk
- first mdk release




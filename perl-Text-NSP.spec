%define module	Text-NSP
%define name	perl-%{module}
%define version 1.09
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	The Ngram Statistics Package 
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Text/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc CHANGES README Docs/*
%{perl_vendorlib}/Text
%{_mandir}/*/*
%{_bindir}/*


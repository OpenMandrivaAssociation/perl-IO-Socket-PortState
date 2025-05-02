%define module IO-Socket-PortState
%undefine _debugsource_packages

Name:		perl-%{module}
Version:	0.03
Release:	1
Summary:	Perl extension for checking the open or closed status of a port
URL:		https://metacpan.org/pod/IO::Socket::PortState
Source:		https://cpan.org/modules/by-module/IO/%{module}-%{version}.tar.gz
License:	Perl (Artistic or GPL)
Group:		Development/Perl
BuildRequires:	perl
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildArch:	noarch

%description
Perl extension for checking the open or closed status of a port

%prep
%autosetup -p1 -n %{module}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install INSTALLDIRS=vendor

%files
%doc Changes MANIFEST README
%{perl_vendorlib}/*/*
%{_mandir}/man3/*.3pm*

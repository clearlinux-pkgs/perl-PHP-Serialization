#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-PHP-Serialization
Version  : 0.34
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/PHP-Serialization-0.34.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/PHP-Serialization-0.34.tar.gz
Summary  : simple flexible means of converting the output of PHP's serialize() into the equivalent Perl memory structure, and vice versa.
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-PHP-Serialization-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
PHP::Serialization - simple flexible means of converting the output of
PHP's serialize() into the equivalent Perl memory structure, and vice
versa.

%package dev
Summary: dev components for the perl-PHP-Serialization package.
Group: Development
Provides: perl-PHP-Serialization-devel = %{version}-%{release}
Requires: perl-PHP-Serialization = %{version}-%{release}

%description dev
dev components for the perl-PHP-Serialization package.


%package perl
Summary: perl components for the perl-PHP-Serialization package.
Group: Default
Requires: perl-PHP-Serialization = %{version}-%{release}

%description perl
perl components for the perl-PHP-Serialization package.


%prep
%setup -q -n PHP-Serialization-0.34
cd %{_builddir}/PHP-Serialization-0.34

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/PHP::Serialization.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*

Summary:	API compatibility checker for Java libraries
Name:		java-api-compliance-checker
Version:	1.1.1
Release:	1
Group:		Development/Other
License:	GPLv1+ or LGPLv2+
URL:		http://ispras.linuxbase.org/index.php/Java_API_Compliance_Checker
Source0:	https://github.com/lvc/japi-compliance-checker/downloads/japi-compliance-checker-%{version}.tar.gz
Requires:	java-openjdk
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Java API Compliance Checker (Java ACC) is a tool for checking backward
binary and source compatibility of a Java library API. The tool checks
classes declarations of old and new versions and analyzes changes that
may break compatibility: removed methods, removed class fields, added
abstract methods, etc. Binary incompatibility may result in crashing or
incorrect behavior of existing clients built with an old version of
a library when they are running with a new one. Source incompatibility
may result in recompilation errors with a new library version. The tool
is intended for library developers and operating system maintainers who
are interested in ensuring backward compatibility, i.e. allow old
clients to run or to be recompiled with newer library versions.

%prep

%setup -q -n japi-compliance-checker-%{version}
chmod 0644 LICENSE README

%build
# Nothing to build.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}
perl Makefile.pl -install --prefix=%{_prefix} --destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE README doc/
%{_bindir}/japi-compliance-checker

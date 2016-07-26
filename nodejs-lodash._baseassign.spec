%{?scl:%scl_package nodejs-lodash._baseassign}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-lodash._baseassign

%global npm_name lodash._baseassign
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-lodash._baseassign
Version:	3.2.0
Release:	1%{?dist}
Summary:	The modern build of lodash’s internal `baseAssign` as a module.
Url:		https://lodash.com/
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:  %{?scl_prefix}runtime

%if 0%{?enable_tests}
%endif

Requires:	%{?scl_prefix}npm(lodash._basecopy)
Requires:	%{?scl_prefix}npm(lodash.keys)

%description
The modern build of lodash’s internal `baseAssign` as a module.

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{!?_licensedir:%global license %doc}
%{nodejs_sitelib}/lodash._baseassign

%doc README.md
%license LICENSE.txt

%changelog
* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 3.2.0-1
- Initial build

%global packname  processx
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          3.2.1
Release:          2%{?dist}
Summary:          Execute and Control System Processes

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-ps, R-R6, R-utils
# Suggests:  R-callr, R-covr, R-crayon, R-debugme, R-parallel, R-testthat, R-withr
# LinkingTo:
# Enhances:

Requires:         R-ps
Requires:         R-R6
Requires:         R-utils
Suggests:         R-crayon
Suggests:         R-debugme
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-ps
BuildRequires:    R-R6
BuildRequires:    R-utils
BuildRequires:    R-callr
BuildRequires:    R-crayon
BuildRequires:    R-debugme
BuildRequires:    R-parallel
BuildRequires:    R-testthat
BuildRequires:    R-withr

%description
Tools to run system processes in the background. It can check if a
background process is running; wait on a background process to finish; get
the exit status of finished processes; kill background processes. It can
read the standard output and error of the processes, using non-blocking
connections. 'processx' can poll a process for standard output or error,
with a timeout. It can also poll several processes at once.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# FIXME: Why does this not install?
install -pm 0644 %{packname}/README.md %{buildroot}%{rlibdir}/%{packname}/


%check
NOT_CRAN=true PROCESSX_EXTRA_TESTS=true %{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/README.md
%doc %{rlibdir}/%{packname}/CODE_OF_CONDUCT.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/bin
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Wed Mar 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.2.1-2
- Enable more tests

* Thu Feb 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.2.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.2.0-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 3.1.0-1
- update to 3.1.0

* Mon May 07 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0.3-1
- Update to latest version

* Wed Mar 21 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.0.1-1
- initial package for Fedora

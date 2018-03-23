%global packname  processx
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.0.1
Release:          1%{?dist}
Summary:          Execute and Control System Processes

License:          MIT
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Patch0001:        0001-Define-BSWAP_32-in-the-correct-place.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-assertthat R-crayon R-debugme R-R6 R-utils
# Suggests:  R-covr R-testthat R-withr
# LinkingTo:
# Enhances:

Requires:         R-assertthat R-crayon R-debugme R-R6 R-utils
BuildRequires:    R-devel tex(latex)
BuildRequires:    R-assertthat R-crayon R-debugme R-R6 R-utils
BuildRequires:    R-testthat R-withr

%description
Portable tools to run system processes in the background. It can check if
a background process is running; wait on a background process to finish;
get the exit status of finished processes; kill background processes and
their children; restart processes. It can read the standard output and
error of the processes, using non-blocking connections. 'processx' can
poll a process for standard output or error, with a timeout. It can also
poll several processes at once.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch0001 -p1
popd

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/README.markdown
%doc %{rlibdir}/%{packname}/internals.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Wed Mar 21 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.0.1-1
- initial package for Fedora

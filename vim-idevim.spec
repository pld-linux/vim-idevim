%define vimver	6.2
%define	vimnver	6.3
Summary:	Control Gdb from inside Vim
Summary(pl):	Obs�uga gdb z VIMa
Name:		vim-idevim
Version:	0.8
Release:	3
License:	GPL
Group:		Applications/Editors/Vim
#Source0:	http://vim.sourceforge.net/scripts/download.php?src_id=428
Source0:	idevim.tgz
# Source0-md5:	b63be71c432a7b67db75dde0afaaefc3
Patch0:		%{name}-Makefile.patch
URL:		http://vim.sourceforge.net/scripts/script.php?script_id=168
BuildRequires:	vim >= %{vimver}
BuildConflicts:	vim >= %{vimnver}
Requires:	vim >= %{vimver}
Conflicts:	vim >= %{vimnver}
Requires:	gdb
Requires(postun):	vim >= %{vimver}
Requires(post):	vim >= %{vimver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		vimshv		%(echo %{vimver} | tr -d .)
%define		_vimdatadir	%{_datadir}/vim/vim%{vimshv}

%description
This is plugin and library which turns Vim into the best Ide in the
world. :-) You can access all the Gdb functions and features; on
execution, the window is split, and the source position is shown in
the top window, while the data appears in the bottom.

%description -l pl
To jest wtyczka i biblioteka, kt�re zmieniaj� VIMa w najlepszy IDE na
�wiecie. :-) Daj� one dost�p do wszystkuch funkcji Gdb. Podczas pracy
debuggera okno jest podzielone: aktualna linia kodu �r�d�oweo pokazana
jest w g�rnym oknie, a dane s� wy�wietlane w dolnym.

%prep
%setup -qn gdbvim
%patch0 -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	VIM_VERSION="%{vimshv}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	VIM_VERSION="%{vimshv}"

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
echo ':helptags %{_vimdatadir}/doc' | vim -e -s

%postun
/sbin/ldconfig
echo ':helptags %{_vimdatadir}/doc' | vim -e -s

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%{_vimdatadir}/doc/*
%{_vimdatadir}/plugin/*

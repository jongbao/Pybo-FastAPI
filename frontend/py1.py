<script>
    import {link} from 'svelte-spa-router'
</script>

<!-- 네이게이션 바 -->
<nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
    <div class="container-fluid">
        <a use:link class="navbar-brand" href="/">Pybo</a>
        <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation">
            <span class="navbar-toggler-icon" />
        </button>
        <div class="collapse navbar-collapse" id="nabvarSupportedContent">
            <ul class="collapse-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <a use:link class="nav-link" href="/user-create">회원가입</a>
                </li>
                <li class="nav-item">
                    <a use:link class="nav-link" href="/user-login">로그인</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
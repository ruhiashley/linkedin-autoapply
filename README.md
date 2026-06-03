# linkedin-autoapply

Automated LinkedIn job application agent built with [browser-use](https://github.com/browser-use/browser-use) and Claude (claude-sonnet) as the LLM backbone.

Built this because manually applying to internships was eating 3-4 hours a week. The agent navigates LinkedIn, filters for relevant roles, and submits Easy Apply applications while I do other things.

## what it does

- loops through a list of search terms (shuffled each run so it doesn't look like a bot)
- filters for Easy Apply only, Internship level, past month
- fills out and submits application forms using your profile info
- uploads resume when the form asks for it
- skips jobs that redirect to external sites or require a cover letter
- randomized delays between applications to avoid rate limiting
- reuses your existing Chrome session so you don't have to log in

## stack

- `browser-use` for browser automation
- `claude-sonnet-4` via `langchain-anthropic` as the agent LLM
- Python 3.12

## setup

```bash
git clone https://github.com/ruhiashley/linkedin-autoapply
cd linkedin-autoapply
uv init
uv add browser-use langchain-anthropic python-dotenv
uvx browser-use install
```

Add your API key:
```bash
cp .env.example .env
# add your ANTHROPIC_API_KEY
```

Update `MY_INFO` and `RESUME_PATH` at the top of `apply.py` with your info.

## usage

Fully quit Chrome first (Cmd+Q), then:

```bash
uv run apply.py
```

## things that didn't work at first

- `BrowserConfig` got renamed to `BrowserProfile` in a recent browser-use update
- `Browser(profile=...)` also broke, needed to be `Browser(BrowserProfile(...))` directly
- agent was applying to senior/staff roles early on, fixed by being more explicit in the task prompt
- LinkedIn rate limiting hit fast without delays, added `asyncio.sleep(random.uniform(3, 8))` between terms

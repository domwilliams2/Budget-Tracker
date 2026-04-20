create table accounts (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users not null,
  name text not null,
  type text not null,  -- 'checking' | 'savings' | 'credit'
  balance numeric default 0,
  created_at timestamptz default now()
);

create table transactions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users not null,
  account_id uuid references accounts not null,
  amount numeric not null,
  category text,
  description text,
  date date not null,
  created_at timestamptz default now()
);

create table budgets (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users not null,
  category text not null,
  amount_limit numeric not null,
  period text not null,  -- 'monthly' | 'weekly'
  created_at timestamptz default now()
);

-- Row Level Security
alter table accounts enable row level security;
alter table transactions enable row level security;
alter table budgets enable row level security;

create policy "users own their accounts"
  on accounts for all using (auth.uid() = user_id);

create policy "users own their transactions"
  on transactions for all using (auth.uid() = user_id);

create policy "users own their budgets"
  on budgets for all using (auth.uid() = user_id);
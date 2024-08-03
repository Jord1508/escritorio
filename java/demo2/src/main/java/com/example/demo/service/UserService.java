package com.example.demo.service;

import com.example.demo.model.User;

import java.util.List;

public interface UserService {
    void add(User customer);

    List<User> all();
}
